import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("nhatki.log", mode="a", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()
  