# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd

import requests
import config
import pickle
import io
from PIL import Image
from flask import jsonify



# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model

disease_dic= ["Alopecia","Folliculitis","Psoriasis"]
disease_dic2= ["stage0","stage1","stage2","stage3","stage4"]


from model_predict  import herbal_hair_care
from model_predict_hair_loss  import herbal_hair_care2
# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------



import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle




import pickle 
app = Flask(__name__)

# render home page


@app.route('/')
def home():
    return render_template('login.html') 

@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
# Save the list as a pickle file
    with open("int_features3.pkl", "wb") as f:
        pickle.dump(int_features3, f)

    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index.html')
    else:
        return jsonify({'result':'Please enter valid credentials'})
                  
                                               



                          
                     # print(value1[0:])
    
    
    
    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this userid is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login.html')

                      


# render crop recommendation form page

@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = ' Classification'

    if request.method == 'POST':
        #if 'file' not in request.files:
         #   return redirect(request.url)
            file = request.files.get('file')

            print(file)
        #if not file:
         #   return render_template('disease.html', title=title)
        #try:
            img1 = file.read()

            #print(img)

            prediction =herbal_hair_care(img1)

            prediction = (str(disease_dic[prediction]))

            print(prediction)
#disease_dic= ["Alopecia","Folliculitis","Psoriasis"]
            if prediction == "Alopecia":
                precaution = "Alopecia is a condition related to hair loss. It is recommended to consult with a dermatologist for proper diagnosis and treatment."
                products_recommendation = ["Minoxidil topical solution", "Biotin supplements", "Gentle hair care products"]
                product_routine = "use Minoxidil topical solution two times a day it give result  4- 6 month ,Biotin supplements take one tablet in a day use mild gentle hair products to wash hair, Leave them on overnight and wash them off with normal wate."


            elif prediction == "Folliculitis":
                 precaution = "Folliculitis is an inflammation of hair follicles. Maintain good hygiene and avoid shaving or using irritating products on affected areas."
                 products_recommendation = ["Antibacterial soap", "Topical antibiotics", "Tea tree oil-based products"]
                 product_routine = "Use the recommended products twice  a daily . Leave them on overnight and wash them off with normal water ,This products gives result 3-4 month ."




            elif prediction == "Psoriasis":
                 precaution = "Psoriasis is a skin condition characterized by red, itchy, and scaly patches. Consult a dermatologist for appropriate management and care."
                 products_recommendation = ["Emollient-rich moisturizers", "Topical corticosteroids", "Salicylic acid-based products"]
                 product_routine = "Use Emollient-rich moisturizers Topical corticosteroids twice  a daily and salicylic ones in daily . Leave them on overnight and wash them off with normal water , This products gives result 4-6 month ."


            return render_template('disease-result.html', prediction=prediction,precaution=precaution,products_recommendation=products_recommendation, product_routine= product_routine,title=title)
        #except:
         #   pass
    return render_template('disease.html', title=title)


# render disease prediction result page
@app.route('/disease-predict2', methods=['GET', 'POST'])
def disease_prediction2():
    title = 'Hairloss classification'

    if request.method == 'POST':
        #if 'file' not in request.files:
         #   return redirect(request.url)
            file = request.files.get('file')

            print(file)
        #if not file:
         #   return render_template('disease.html', title=title)
        #try:
            img1 = file.read()

            #print(img)

            prediction =herbal_hair_care2(img1)

            prediction = (str(disease_dic2[prediction]))

            print(prediction)
            #disease_dic= ["Alopecia","Folliculitis","Psoriasis"]
            # disease_dic= ["Alopecia","Folliculitis","Psoriasis"]
            if prediction == "stage0":
                precaution = "better go with below prescription for better results in next phase of treatment"
                products_recommendation = ["Minoxidil topical solution", "Biotin supplements", "Gentle hair care products"]
                

            elif prediction == "stage1":
                precaution = "better go with below prescription for better results in next phase of treatment"
                products_recommendation = ["Antibacterial soap", "Topical antibiotics", "Tea tree oil-based products"]

            elif prediction == "stage2":
                precaution = "better go with below prescription for better results in next phase of treatment"
                products_recommendation = ["Emollient-rich moisturizers", "Topical corticosteroids", "Salicylic acid-based products"]

            elif prediction == "stage3":
                precaution = "better go with below prescription for better results in next phase of treatment"
                products_recommendation = ["Emollient-rich moisturizers", "Topical corticosteroids", "Salicylic acid-based products"]

            elif prediction == "stage4":
                precaution = "better go with below prescription for better results in next phase of treatment"
                products_recommendation = ["Wigs or hairpieces", "Scalp micropigmentation services", "Scalp care products for maintaining a healthy scalp"]
            # Load the pickle file
            with open("int_features3.pkl", "rb") as f:
                loaded_int_features3 = pickle.load(f)


            print("the user login information is ",loaded_int_features3)

            import os
            import pandas as pd
            # Check if the CSV file already exists
            file_name = loaded_int_features3[0] + ".csv"
            if os.path.isfile(file_name):
                # If the file exists, load existing data
                df = pd.read_csv(file_name)
            else:
                    # If the file doesn't exist, create a new DataFrame
                    df = pd.DataFrame(columns=['stage', 'treatment', 'date'])
                    # Write the DataFrame to a CSV file
                    df.to_csv(file_name, index=False)
            print(df)

            from datetime import datetime

            # Get the current date and time
            current_datetime = datetime.now()

            # Format the date and time as a string
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            print("Current date and time:", formatted_datetime)
            # Manually create a DataFrame with three values for each column
            new_data = {
                'stage': [prediction],
                'treatment': [products_recommendation],
                'date': [formatted_datetime]
            }
            df_new = pd.DataFrame(new_data)

            # Append new data to existing DataFrame
            df = df.append(df_new, ignore_index=True)

            df.to_csv(loaded_int_features3[0] + ".csv",index=False)

            try:
                   df = df.drop(columns=['Unnamed: 0'])
            except:

                   print("no unnamed column created")

            # Define the directory containing images


            folder_name=prediction
            image_folder = os.path.join('static', 'images', folder_name)

            # Check if the specified folder exists
            if not os.path.exists(image_folder):
                abort(404)

            # Get the list of image filenames in the directory
            image_files = os.listdir(image_folder)




            return render_template('disease-result2.html', prediction=prediction,precaution=precaution,products_recommendation=products_recommendation,title=title,table=df.to_html(),image_files=image_files, folder_name=folder_name)
        #except:
         #   pass
    return render_template('disease2.html', title=title)
# ==============================================================================================
# Importing essential libraries and modules
import os  
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt  
from datetime import datetime 
@app.route('/plot')
def plot_graph():
    # Assuming this part loads your DataFrame correctly
    with open("int_features3.pkl", "rb") as f:
        loaded_int_features3 = pickle.load(f)
    
    file_name = loaded_int_features3[0] + ".csv"
    if not os.path.isfile(file_name):
        #return "CSV file does not exist."
        return jsonify({'file_name': 'CSV file does not exist.', 'message': 'The DataFrame is empty'})

    
    df = pd.read_csv(file_name)

    if df.empty:
        return jsonify({"The DataFrame is empty."})
         

    # Ensure 'date' is a datetime type and set as index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Ensure data is sorted by date
    df.sort_index(inplace=True)

    # Define colors for each stage
    stage_colors = {
        'stage0': 'blue',
        'stage1': 'green',
        'stage2': 'orange',
        'stage3': 'red',
        'stage4': 'purple'
    }

    # Create an empty figure and axis for plotting
    plt.figure(figsize=(10, 6))

    # Plot each stage in the DataFrame with its corresponding color
    for stage, color in stage_colors.items():
        # Filter rows where 'stage' matches the current stage in the loop
        stage_df = df[df['stage'] == stage]
        
        # Plot each date of the current stage
        plt.plot_date(stage_df.index, [stage]*len(stage_df), linestyle='-', marker='o', label=stage, color=color)

    # Add legend, labels, and title
    plt.legend()
    plt.xlabel('Dates')
    plt.ylabel('Stages')
    plt.title('Stages Distribution Over Time')
    plt.xticks(rotation=45)  # Rotate dates for better visibility

    # Save the plot as a PNG file
    plt.tight_layout()
    plt.savefig('static/images/bar_plot.png')
    plt.close()  # Close the plot to free up memory

    # Return the path to the generated plot
    return render_template('plot.html', image_file='/static/images/bar_plot.png')
#===============================================================================================
import os  
from flask import Flask, render_template
import pandas as pd
@app.route('/suggestion')
def def_suggestion():
    return render_template('herbalsolution.html')
    


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
