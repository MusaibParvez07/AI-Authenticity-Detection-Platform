from backend.ai.image.build_dataset import (
    dataset_builder,
)

dataset_builder.build(

    image_dir="datasets/image",

    label="unknown",

    output_csv="datasets/features/image_features.csv",

)