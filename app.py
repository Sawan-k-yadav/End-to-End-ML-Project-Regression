from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),   # Doing type casting for all feilds which are coming from the web page as string
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),     # Not defining type of categorical feature as it wil be handle by preprocessor
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )

        # converting my custom data to dataframe
        final_new_data=data.get_data_as_dataframe()
        # final_new_data=data.get_data_as_dataframe()

        # doing prediction with dataframe data
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)
        print(type(pred))

        results=round(pred[0],2)  # Here prediction will come in array so we will take 0th value or we can jsonify
        # results=round(pred[0],2)
        return render_template('result.html',final_result=results)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)