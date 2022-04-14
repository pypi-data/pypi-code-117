import os
# from neuron_tracing.lib.pyneval.metric.utils import cli_utils
from neuron_tracing.lib.swclib.exceptions import InvalidSwcFileError
from neuron_tracing.lib.swclib.swc_tree import SwcTree


def is_swc_file(file_path):
    return file_path[-4:] in (".swc", ".SWC")


def read_swc_tree(swc_file_path):
    if not os.path.isfile(swc_file_path) or not is_swc_file(swc_file_path):
        raise InvalidSwcFileError(swc_file_path)
    swc_tree = SwcTree()
    swc_tree.load(swc_file_path)
    return swc_tree


# if path is a folder
# def read_swc_trees(swc_file_paths, tree_name_dict=None):
#     """
#     Read a swc tree or recursively read all the swc trees in a fold
#     Args:
#         swc_file_paths(string): path to read swc
#         tree_name_dict(dict): a map for swc tree and its file name
#             key(SwcTree): SwcTree object
#             value(string): name of the swc tree
#     Output:
#         swc_tree_list(list): a list shaped 1*n, containing all the swc tree in the path
#     """
#     # get all swc files
#     swc_files = []
#     if os.path.isfile(swc_file_paths):
#         if not is_swc_file(swc_file_paths):
#             print(swc_file_paths + "is not a swc file")
#             return
#         swc_files = [swc_file_paths]
#     else:
#         for root, _, files in os.walk(swc_file_paths):
#             for file in files:
#                 f = os.path.join(root, file)
#                 if is_swc_file(f):
#                     swc_files.append(f)
#     # load swc trees
#     swc_tree_list = []
#     for swc_file in swc_files:
#         swc_tree = SwcTree()
#         swc_tree.load(swc_file)
#         swc_tree_list.append(swc_tree)
#         if tree_name_dict is not None:
#             tree_name_dict[swc_tree] = os.path.basename(swc_file)
#     return swc_tree_list


# def adjust_swcfile(swc_str):
#     words = swc_str.split("\n")
#     return words
#
#
# def read_from_str(swc_str):
#     swc_tree = swc_tree.SwcTree()
#     swc_list = adjust_swcfile(swc_str)
#     swc_tree.load_list(swc_list)
#     return swc_tree


def swc_save(swc_tree, out_path, extra=None):
    out_path = os.path.normpath(out_path)
    swc_tree.sort_node_list(key="compress")
    swc_node_list = swc_tree.get_node_list()

    if not os.path.exists(os.path.dirname(out_path)):
        os.mkdir(os.path.dirname(out_path))

    with open(out_path, "w") as f:
        f.truncate()
        if extra is not None:
            f.write(extra)
        for node in swc_node_list:
            if node.is_virtual():
                continue
            try:
                f.write(
                    "{} {} {} {} {} {} {}\n".format(
                        node.get_id(),
                        node._type,
                        node.get_x(),
                        node.get_y(),
                        node.get_z(),
                        node.radius(),
                        node.parent.get_id(),
                    )
                )
            except:
                continue
    return True

def swc_save_metric(save_dir, swc_data):
    with open(save_dir, 'w') as fp:
        for i in range(swc_data.shape[0]):
            fp.write('%d %d %g %g %g %g %d\n' % (
                swc_data[i][0], swc_data[i][1], swc_data[i][2], swc_data[i][3], swc_data[i][4], swc_data[i][5],
                swc_data[i][6]))
        fp.close()

if __name__ == "__main__":
    from pyneval.model import swc_node
    tree = SwcTree()
    tree.load("E:\\04_code\\00_neural_reconstruction\PyNeval\data\default.0.swc")
    swc_save(tree, "E:\\04_code\\00_neural_reconstruction\PyNeval\data\default.1.swc")