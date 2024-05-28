from asyncflows.scripts.generate_config_schema import _build_and_save_asyncflows_schema
from asyncflows.models.config.flow import (
    ActionConfig,
)

from asyncflows.actions import get_actions_dict

# import custom actions here
import my_actions.load_json
import my_actions.create_string

_action_names = list(get_actions_dict().keys())


_build_and_save_asyncflows_schema(
    action_names=_action_names,
    config_class=ActionConfig,
    output_file="custom_asyncflows_schema.json",
    strict=False,
)       
