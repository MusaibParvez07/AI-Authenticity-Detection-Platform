"""
Train Fusion Model

Learns how to combine all forensic
features into one final prediction.
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


class FusionTrainer:

    def train(
        self,
        csv_file,
        model_path,
    ):

        csv_file = Path(csv_file)

        model_path = Path(model_path)

        df = pd.read_csv(csv_file)

        # ---------------------------------------
        # Convert AI Prediction
        # ---------------------------------------

        df["ai_prediction"] = df["ai_prediction"].map({

            "real": 1,

            "fake": 0,

        })

        # ---------------------------------------
        # Remove filename
        # ---------------------------------------

        if "filename" in df.columns:

            df = df.drop(

                columns=["filename"]

            )

        # ---------------------------------------
        # Label Encoding
        # ---------------------------------------

        df["label"] = df["label"].map({

            "real": 1,

            "fake": 0,

        })

        # ---------------------------------------

        X = df.drop(

            columns=["label"]

        )

        y = df["label"]

        # ---------------------------------------

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y,

        )

        # ---------------------------------------

        model = RandomForestClassifier(

            n_estimators=300,

            random_state=42,

            n_jobs=-1,

        )

        model.fit(

            X_train,

            y_train,

        )

        # ---------------------------------------

        pred = model.predict(

            X_test

        )

        print()

        print("=" * 60)

        print("Accuracy")

        print(

            accuracy_score(

                y_test,

                pred,

            )

        )

        print()

        print(

            classification_report(

                y_test,

                pred,

            )

        )

        print("=" * 60)

        model_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        joblib.dump(

            model,

            model_path,

        )

        print()

        print("Model Saved")

        print(model_path)


fusion_trainer = FusionTrainer()