# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Helper utilities for use while testing examples.

isort:skip_file
"""
import os
import sys

os.environ["AWS_ENCRYPTION_SDK_EXAMPLES_TESTING"] = "yes"
sys.path.extend([os.sep.join([os.path.dirname(__file__), "..", "..", "test", "integration"])])

# fmt: off
from integration_test_utils import cmk_arn, cmk_mrk_arn, ddb_table_name, second_cmk_mrk_arn  # noqa pylint: disable=unused-import
# fmt: on
