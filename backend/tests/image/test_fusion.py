from backend.ai.image.train_fusion_model import (
    fusion_trainer,
)

fusion_trainer.train(

    csv_file="datasets/features/image_features.csv",

    model_path="backend/weights/image/fusion/random_forest.pkl",

)