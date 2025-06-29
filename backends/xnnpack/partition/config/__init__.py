# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from typing import List, Type

from executorch.backends.xnnpack.partition.config.gemm_configs import (
    AddmmConfig,
    ConvolutionConfig,
    LinearConfig,
    MMConfig,
)

from executorch.backends.xnnpack.partition.config.generic_node_configs import (
    AbsConfig,
    AddConfig,
    AvgPoolingConfig,
    BMMConfig,
    CatConfig,
    CeilConfig,
    ClampConfig,
    ConstantPadConfig,
    DeQuantizedPerTensorConfig,
    DivConfig,
    FloorConfig,
    GeluConfig,
    HardswishConfig,
    # EluConfig,
    HardtanhConfig,
    LeakyReLUConfig,
    LogConfig,
    MaximumConfig,
    MaxPool2dConfig,
    MeanDimConfig,
    MinimumConfig,
    MulConfig,
    NegConfig,
    PermuteConfig,
    PowConfig,
    QuantizedPerTensorConfig,
    ReciprocalSquareRootConfig,
    ReLUConfig,
    # SDPAConfig, TODO: D60553559: preserving SDPA for fairseq fails
    SigmoidConfig,
    SliceCopyConfig,
    SoftmaxConfig,
    SquareRootConfig,
    SubConfig,
    TanhConfig,
    UpsampleBilinear2dConfig,
)
from executorch.backends.xnnpack.partition.config.node_configs import (
    BatchNormConfig,
    MaxDimConfig,
    PreluConfig,
)
from executorch.backends.xnnpack.partition.config.quant_affine_configs import (
    ChooseQParamsAffineConfig,
    DeQuantizeAffineConfig,
    QuantizeAffineConfig,
)
from executorch.backends.xnnpack.partition.config.xnnpack_config import (
    XNNPartitionerConfig,
)

ALL_PARTITIONER_CONFIGS: List[Type[XNNPartitionerConfig]] = [
    AbsConfig,
    AddConfig,
    AddmmConfig,
    AvgPoolingConfig,
    BatchNormConfig,
    BMMConfig,
    CatConfig,
    CeilConfig,
    ConstantPadConfig,
    ConvolutionConfig,
    ClampConfig,
    DivConfig,
    # EluConfig, # Waiting for PyTorch Pin Update
    FloorConfig,
    GeluConfig,
    HardtanhConfig,
    HardswishConfig,
    LeakyReLUConfig,
    LinearConfig,
    LogConfig,
    MaxDimConfig,
    MaximumConfig,
    MaxPool2dConfig,
    MeanDimConfig,
    MinimumConfig,
    MMConfig,
    MulConfig,
    NegConfig,
    PermuteConfig,
    PowConfig,
    PreluConfig,
    ReciprocalSquareRootConfig,
    ReLUConfig,
    TanhConfig,
    # SDPAConfig, TODO: D60553559: preserving SDPA for fairseq fails
    SigmoidConfig,
    SliceCopyConfig,
    SoftmaxConfig,
    SquareRootConfig,
    SubConfig,
    UpsampleBilinear2dConfig,
    # Quant/Dequant Op Configs
    QuantizedPerTensorConfig,
    DeQuantizedPerTensorConfig,
    # Quant Affine Configs to preserve decomp
    QuantizeAffineConfig,
    DeQuantizeAffineConfig,
    ChooseQParamsAffineConfig,
]
