from flask import Flask, render_template, jsonify, request
import pandas as pd
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'MySqL_JNJ13!'
# app.config['MYSQL_DB'] = 'DataBootCamp'

# mysql = MySQL(app)

# @app.route('/', methods=['POST'])
# def index():
#     if request.method == 'POST':
#         detail = request.form
#         first_name = detail['first_name']
#         last_name = detail['last_name']
#         cur = mysql.connection.cursor()
#         cur.execute ("INSERT INTO MyUsers(first_name, last_name) VALUES (%s, %s)")
#         mysql.connection.commit()
#         cur.close()
#         return 'success'

# @app.route('/')
# def index():
#     return 'Hello'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        req = request.form

        industry_partner = req['industry_partner']
        client_id = req['client_id']
        travel_no = req['travel_no']
        dt = req['dt']
        project_name = req['project_name']
        project_id = req['project_id']
        contract_task_order = req['contract_task_order']
        
        from_requestor = req['from_requestor']
        through = req['client_id']
        try:
            funding_stream = req.get('funding_stream')
            # if funding_stream!=None:
            #     funding_stream = funding_stream
            # else:
            #     funding_stream = 'error'
        except:
            funding_stream = "didn't work"
        subject_id = req['subject_id']
        cum_amt_billed = req['cum_amt_billed']
        cum_amt_billed_balance = req['cum_amt_billed_balance']
        estimate = req['estimate']
        estimate_balance = req['estimate_balance']

        client_poc = req['client_poc']
        id_project_mgr = req['id_project_mgr']
        travel_justification = req['travel_justification']
        first_name = req['first_name']
        middle_name = req['middle_name']
        last_name = req['last_name']
        company = req['company']
        sub_company_poc_name = req['sub_company_poc_name']
        sub_company_address = req['sub_company_address']
        sub_company_city = req['sub_company_city']
        sub_company_phone = req['sub_company_phone']
        sub_company_email = req['sub_company_email']
        sub_company_po = req['sub_company_po']
        
        birth_date = req['birth_date']
        place_of_birth = req['place_of_birth']
        ssn = req['ssn']
        dod_id = req['dod_id']
        passport_no = req['passport_no']
        passport_expiration = req['passport_expiration']
        employee_id = req['employee_id']
        date_hired = req['date_hired']
        position_type = req['position_type']
        primary_phone = req['primary_phone']
        primary_email = req['primary_email']
        secondary_email = req['secondary_email']
        task_id = req['task_id']
        manager = req['manager']
        oy2_po_code = req['oy2_po_code']
        oy2_org_code = req['oy2_org_code']
        oy2_project_string = req['oy2_project_string']
        plc_code = req['plc_code']
        nok_date = req['nok_date']
        fsde_sheet_date = req['fsde_sheet_date']
        deployment_start_date = req['deployment_start_date']
        deployment_end_date = req['deployment_end_date']
        leave_start_date = req['leave_start_date']
        leave_end_date = req['leave_end_date']
        mil_leave_start_date = req['mil_leave_start_date']
        mil_leave_end_date = req['mil_leave_end_date']
        
        ditac = req['ditac']
        sis = req['sis']
        ftp = req['ftp']
        jasa = req['jasa']
        dst_osint = req['dst_osint']
        proton = req['proton']
        fmv_academy = req['fmv_academy']
        
        ccmsubmit = req['ccmsubmit']
        ci_brief = req['ci_brief']
        visa_submitted = req['visa_submitted']
        src_date = req['src_date']
        src_travel_submission = req['src_travel_submission']
        deployment_travel_submission = req['deployment_travel_submission']

        # cur = mysql.connection.cursor()
        # cur.execute ("INSERT INTO MyUsers(first_name, last_name) VALUES (%s, %s)")
        # mysql.connection.commit()
        # cur.close()
        
        client_dict = {
            'industry_partner':industry_partner,
            'client_id':client_id,
            'travel_no':travel_no,
            'dt':dt,
            'project_name':project_name,
            'project_id':project_id,
            'contract_task_order':contract_task_order
            }
        
        tpoc_dict = {
            'from_requestor':from_requestor,
            'through':through,
            'funding_stream':funding_stream,
            'subject_id':subject_id,
            'cum_amt_billed':cum_amt_billed,
            'cum_amt_billed_balance':cum_amt_billed_balance,
            'estimate':estimate,
            'estimate_balance':estimate_balance
        }

        traveler_dict = {
            'client_poc':client_poc,
            'id_project_mgr':id_project_mgr,
            'travel_justification':travel_justification,
            'first_name':first_name,
            'middle_name':middle_name,
            'last_name':last_name,
            'company':company,
            'sub_company_poc_name':sub_company_poc_name,
            'sub_company_address':sub_company_address,
            'sub_company_city':sub_company_city,
            'sub_company_phone':sub_company_phone,
            'sub_company_email':sub_company_email,
            'sub_company_po':sub_company_po,
        }

        employee_dict = {
            'birth_date':birth_date,
            'place_of_birth':place_of_birth,
            'ssn':ssn,
            'dod_id':dod_id,
            'passport_no':passport_no,
            'passport_expiration':passport_expiration,
            'employee_id':employee_id,
            'date_hired':date_hired,
            'position_type':position_type,
            'primary_phone':primary_phone,
            'primary_email':primary_email,
            'secondary_email':secondary_email,
            'task_id':task_id,
            'manager':manager,
            'oy2_po_code':oy2_po_code,
            'oy2_org_code':oy2_org_code,
            'oy2_project_string':oy2_project_string,
            'plc_code':plc_code,
            'nok_date':nok_date,
            'fsde_sheet_date':fsde_sheet_date,
            'deployment_start_date':deployment_start_date,
            'deployment_end_date':deployment_end_date,
            'leave_start_date':leave_start_date,
            'leave_end_date':leave_end_date,
            'mil_leave_start_date':mil_leave_start_date,
            'mil_leave_end_date':mil_leave_end_date
        }

        training_dict = {
            'ditac':ditac,
            'sis':sis,
            'ftp':ftp,
            'jasa':jasa,
            'dst_osint':dst_osint,
            'proton':proton,
            'fmv_academy':fmv_academy
        }

        task_dict = {
            'ccmsubmit':ccmsubmit,
            'ci_brief':ci_brief,
            'visa_submitted':visa_submitted,
            'src_date':src_date,
            'src_travel_submission':src_travel_submission,
            'deployment_travel_submission':deployment_travel_submission
        }


        tables = [
            client_dict,
            tpoc_dict,
            traveler_dict,
            employee_dict,
            training_dict,
            task_dict
        ]

        # data_df = pd.DataFrame([data_dict])
        # data_df.to_csv('input.csv')
        return jsonify(tables)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)