import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="hydra_conf_mgnt")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(f"User: {cfg.db.user}")
    print(f"Password: {cfg.db['pass']}")

if __name__ == "__main__":
    my_app()
# Run with: python hydra_conf_mgnt.py db.user=root db.pass=1234