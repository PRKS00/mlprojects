from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictData', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Collect data from form inputs
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("✅ Input DataFrame:\n", pred_df)

            # Predict using model
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Render result
            return render_template('home.html', results=round(results[0], 2))

        except Exception as e:
            print(f"❌ Error: {e}")
            return render_template('home.html', results="Error in prediction. Check input values.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
