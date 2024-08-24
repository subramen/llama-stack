# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import List

from llama_toolchain.distribution.datatypes import Api, InlineProviderSpec, ProviderSpec


def available_inference_providers() -> List[ProviderSpec]:
    return [
        InlineProviderSpec(
            api=Api.memory,
            provider_id="meta-reference-faiss",
            pip_packages=[
                "faiss",
                "sentence-transformers",
            ],
            module="llama_toolchain.memory.meta_reference.faiss",
            config_class="llama_toolchain.memory.meta_reference.faiss.FaissImplConfig",
        ),
    ]
