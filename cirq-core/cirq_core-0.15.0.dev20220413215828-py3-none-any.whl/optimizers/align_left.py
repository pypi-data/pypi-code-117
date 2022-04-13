# Copyright 2021 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An optimization pass that aligns gates to the left of the circuit."""

from cirq import circuits
from cirq.circuits.insert_strategy import InsertStrategy
from cirq._compat import deprecated_class


@deprecated_class(deadline='v1.0', fix='Use cirq.align_left(circuit, context) instead.')
class AlignLeft:
    """Aligns gates to the left of the circuit."""

    def __call__(self, circuit: circuits.Circuit):
        self.optimize_circuit(circuit)

    def optimize_circuit(self, circuit: circuits.Circuit):
        circuit[:] = circuits.Circuit(circuit.all_operations(), strategy=InsertStrategy.EARLIEST)
