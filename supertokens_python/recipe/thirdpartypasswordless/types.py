# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from typing import Union

from ..thirdparty.types import ThirdPartyInfo


class User:
    def __init__(self, user_id: str,
                 email: Union[str, None], phone_number: Union[str, None], third_party_info: Union[ThirdPartyInfo, None], time_joined: int):
        self.user_id: str = user_id
        self.email: Union[str, None] = email
        self.phone_number: Union[str, None] = phone_number
        self.time_joined: int = time_joined
        self.third_party_info: Union[ThirdPartyInfo, None] = third_party_info
