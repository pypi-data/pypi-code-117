import argparse
import re
import shutil
from pathlib import Path

import git


def main() -> None:
    parser = argparse.ArgumentParser(description="HiFi-GAN+ Model Checkpoint Cloner")
    parser.add_argument(
        "source_model",
        help="source model prefix",
    )
    parser.add_argument(
        "target_model",
        help="target model prefix",
    )
    parser.add_argument(
        "--checkpoint",
        help="checkpoint number to transfer (defaults to latest)",
    )
    parser.add_argument(
        "--log_path",
        type=Path,
        default="logs",
        help="training log root path",
    )

    args = parser.parse_args()

    # construct the source/target log paths
    source_paths = sorted(args.log_path.glob(f"{args.source_model}*"))
    if not source_paths:
        raise Exception(f"source model {args.source_model} not found")
    source_path = source_paths[0]
    git_hash = git.Repo().head.object.hexsha[:7]
    target_path = args.log_path / f"{args.target_model}-{git_hash}"
    target_path.mkdir(exist_ok=True)

    # remove checkpoints from the target
    for path in target_path.glob("ckpt-*"):
        path.unlink()

    # copy any auxiliary files
    for path in source_path.iterdir():
        if not re.match(r"(ckpt-)|wandb$", path.name):
            if path.is_dir():
                shutil.copytree(path, target_path / path.name, dirs_exist_ok=True)
            else:
                shutil.copy2(path, target_path)

    # copy the requested/latest checkpoint
    ckpt_paths = sorted(source_path.glob(f"ckpt-{args.checkpoint or '*'}k.pt"))
    if not ckpt_paths:
        raise Exception("checkpoint not found")
    checkpoint = ckpt_paths[-1]
    shutil.copy2(checkpoint, target_path)

    print(f"copied {source_path.name}/{checkpoint.name} to {target_path.name}")


if __name__ == "__main__":
    main()
