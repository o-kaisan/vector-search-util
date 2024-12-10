import os
import yaml
from typing import Union

class Config:

    @classmethod
    def load_config(cls, config_path: str = "config/config.yaml") -> dict:
        """
        設定ファイルを読み込む
        注意：必ずルートディレクトリから実行すること
        """
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
