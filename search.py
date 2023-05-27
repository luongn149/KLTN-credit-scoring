import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nvluong1990",
    database="kltn"
)
cursor = db.cursor()

def searchdata():
    global myresult
    id = e1.get()
    name = e2.get()
    age_get = e3.get()
    academic_lv_get = e4.get()
    marital_stt_get = e5.get()
    children_get = e6.get()
    month_income_get = e7.get()
    seniority_get = e8.get()
    employment_contract_get = e9.get()
    bike_property_value_get = e10.get()
    house_property_value_get = e11.get()
    other_property_value_get = e12.get()
    owned_debt_get = e13.get()
    finished_transaction_get = e14.get()

    try:
        cursor.execute("SELECT * FROM mytable where id = '" + id + "'")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        e2.delete(0, END)
        e2.insert(END, x[1])
        e3.delete(0, END)
        e3.insert(END, x[2])
        e4.delete(0, END)
        e4.insert(END, x[3])
        e5.delete(0, END)
        e5.insert(END, x[4])
        e6.delete(0, END)
        e6.insert(END, x[5])
        e7.delete(0, END)
        e7.insert(END, x[6])
        e8.delete(0, END)
        e8.insert(END, x[7])
        e9.delete(0, END)
        e9.insert(END, x[8])
        e10.delete(0, END)
        e10.insert(END, x[9])
        e11.delete(0, END)
        e11.insert(END, x[10])
        e12.delete(0, END)
        e12.insert(END, x[11])
        e13.delete(0, END)
        e13.insert(END, x[12])
        e14.delete(0, END)
        e14.insert(END, x[13])

    except Exception as e:
       print(e)
       db.rollback()
       db.close()
    return age_get, academic_lv_get, marital_stt_get, children_get, month_income_get, seniority_get, employment_contract_get, bike_property_value_get, house_property_value_get, other_property_value_get, owned_debt_get, finished_transaction_get

def credit():
    value = searchdata()
    age_get = value[0]
    academic_lv_get = value[1]
    marital_stt_get = value[2]
    children_get = value[3]
    month_income_get = value[4]
    seniority_get = value[5]
    employment_contract_get = value[6]
    bike_property_value_get = value[7]
    house_property_value_get = value[8]
    other_property_value_get = value[9]
    owned_debt_get = value[10]
    finished_transaction_get = value[11]

    age = ctrl.Antecedent(np.arange(18, 65, 1), 'tuoi')
    academic_lv = ctrl.Antecedent(np.arange(1, 3, 0.1), 'trinh_do_hoc_van')
    marital_stt = ctrl.Antecedent(np.arange(0, 1, 0.1), 'tinh_trang_hon_nhan')
    children = ctrl.Antecedent(np.arange(1, 5, 0.1), 'so_con')
    month_income = ctrl.Antecedent(np.arange(2900, 20000, 1), 'thu_nhap_hang_thang')
    seniority = ctrl.Antecedent(np.arange(0, 15, 0.1), 'tham_nien')
    employment_contract = ctrl.Antecedent(np.arange(0, 2, 0.1), 'loai_hop_dong')
    bike_property_value = ctrl.Antecedent(np.arange(15000, 80000, 1), 'gia_tri_tai_san_phuong_tien')
    house_property_value = ctrl.Antecedent(np.arange(0, 1500000, 1), 'gia_tri_tai_san_nha_o')
    other_property_value = ctrl.Antecedent(np.arange(10000, 80000, 1), 'gia_tri_tai_san_khac')
    owned_debt = ctrl.Antecedent(np.arange(0, 3, 0.1), 'khoan_no_hien_co')
    finished_transaction = ctrl.Antecedent(np.arange(0, 3, 0.1), 'giao_dich_da_hoan_tat')
    over_rated = ctrl.Consequent(np.arange(0, 1, 0.1), 'ket_qua')
    nhankhau = ctrl.Consequent(np.arange(0, 3, 0.1), 'nhan_khau_hoc')
    taichinh = ctrl.Consequent(np.arange(0, 3, 0.1), 'tai_chinh')
    taisan = ctrl.Consequent(np.arange(0, 3, 0.1), 'tai_san_dam_bao')
    tindung = ctrl.Consequent(np.arange(0, 3, 0.1), 'muc_tin_dung')
    nhankhau1 = ctrl.Antecedent(np.arange(0, 3, 0.1), 'nhan_khau_hoc1')
    taichinh1 = ctrl.Antecedent(np.arange(0, 3, 0.1), 'tai_chinh1')
    taisan1 = ctrl.Antecedent(np.arange(0, 3, 0.1), 'tai_san_dam_bao1')
    tindung1 = ctrl.Antecedent(np.arange(0, 3, 0.1), 'muc_tin_dung1')

    ###tap mo###
    # tuoi
    age['tre'] = fuzz.trapmf(age.universe, [18, 18, 27, 33])
    age['trung nien'] = fuzz.trapmf(age.universe, [27, 33, 48, 53])
    age['gia'] = fuzz.trapmf(age.universe, [48, 53, 65, 65])

    # trinh do hoc van
    academic_lv['thap'] = fuzz.trapmf(academic_lv.universe, [0, 0, 0.8, 1])
    academic_lv['trung binh'] = fuzz.trapmf(academic_lv.universe, [0.8, 1, 1.5, 2.25])
    academic_lv['cao'] = fuzz.trapmf(academic_lv.universe, [1.5, 2.25, 3, 3])

    # tinh trang hon nhan
    marital_stt['doc than'] = fuzz.trapmf(marital_stt.universe, [0, 0, 0.7, 0.7])
    marital_stt['co gia dinh'] = fuzz.trapmf(marital_stt.universe, [0.7, 0.7, 1, 1])

    # so con
    children['it'] = fuzz.trapmf(children.universe, [0, 0, 1, 2])
    children['vua'] = fuzz.trapmf(children.universe, [1, 2, 3, 3.7])
    children['nhieu'] = fuzz.trapmf(children.universe, [3, 3.7, 5, 5])

    # thu nhap hang thang
    month_income['thap'] = fuzz.trapmf(month_income.universe, [2900, 2900, 5500, 6000])
    month_income['trung binh'] = fuzz.trapmf(month_income.universe, [5500, 6000, 10000, 12000])
    month_income['cao'] = fuzz.trapmf(month_income.universe, [10000, 12000, 20000, 20000])

    # tham nien cong tac
    seniority['ngan'] = fuzz.trapmf(seniority.universe, [0, 0, 3.5, 4])
    seniority['trung binh'] = fuzz.trapmf(seniority.universe, [3.5, 4, 8, 8.5])
    seniority['dai'] = fuzz.trapmf(seniority.universe, [8, 8.5, 15, 15])

    # loai hop dong lao dong
    employment_contract['thoi vu'] = fuzz.trapmf(employment_contract.universe, [0, 0, 1, 1])
    employment_contract['co thoi han'] = fuzz.trapmf(employment_contract.universe, [0.5, 0.5, 1.5, 1.5])
    employment_contract['khong thoi han'] = fuzz.trapmf(employment_contract.universe, [1, 1, 2, 2])

    # gia tri tai san phuong tien
    bike_property_value['re'] = fuzz.trapmf(bike_property_value.universe, [15000, 15000, 20000, 25000])
    bike_property_value['vua'] = fuzz.trapmf(bike_property_value.universe, [20000, 25000, 50000, 60000])
    bike_property_value['dat'] = fuzz.trapmf(bike_property_value.universe, [50000, 60000, 80000, 80000])

    # gia tri tai san nha o
    house_property_value['thap'] = fuzz.trapmf(house_property_value.universe, [0, 0, 350000, 450000])
    house_property_value['trung binh'] = fuzz.trapmf(house_property_value.universe, [350000, 450000, 800000, 1000000])
    house_property_value['cao'] = fuzz.trapmf(house_property_value.universe, [800000, 1000000, 1500000, 1500000])

    # gia tri tai san khac
    other_property_value['thap'] = fuzz.trapmf(other_property_value.universe, [10000, 10000, 20000, 22500])
    other_property_value['trung binh'] = fuzz.trapmf(other_property_value.universe, [20000, 22500, 47500, 50000])
    other_property_value['cao'] = fuzz.trapmf(other_property_value.universe, [47500, 50000, 80000, 80000])

    # khoan no hien co
    owned_debt['khong no'] = fuzz.trimf(owned_debt.universe, [0, 0, 0.8])
    owned_debt['no it'] = fuzz.trimf(owned_debt.universe, [0.8, 1.3, 1.8])
    owned_debt['no nhieu'] = fuzz.trimf(owned_debt.universe, [1.6, 3, 3])

    # so giao dich da hoan tat
    finished_transaction['yeu'] = fuzz.trimf(finished_transaction.universe, [0, 0, 0.9])
    finished_transaction['trung binh'] = fuzz.trimf(finished_transaction.universe, [0.7, 1.2, 2])
    finished_transaction['manh'] = fuzz.trimf(finished_transaction.universe, [1.9, 3, 3])

    # ket qua xep hang
    over_rated['rui ro cao'] = fuzz.trapmf(over_rated.universe, [0, 0, 0.3, 0.3])
    over_rated['rui ro trung binh'] = fuzz.trapmf(over_rated.universe, [0.3, 0.3, 0.7, 0.7])
    over_rated['rui ro thap'] = fuzz.trapmf(over_rated.universe, [0.7, 0.7, 1, 1])

    # nhan khau hoc
    nhankhau['yeu'] = fuzz.trapmf(nhankhau.universe, [0, 0, 0.5, 1])
    nhankhau['trung binh'] = fuzz.trapmf(nhankhau.universe, [0.5, 1, 1.5, 2])
    nhankhau['manh'] = fuzz.trapmf(nhankhau.universe, [1.5, 2, 2.5, 3])

    # tai chinh
    taichinh['yeu'] = fuzz.trapmf(taichinh.universe, [0, 0, 0.5, 1])
    taichinh['trung binh'] = fuzz.trapmf(taichinh.universe, [0.5, 1, 1.5, 2])
    taichinh['manh'] = fuzz.trapmf(taichinh.universe, [1.5, 2, 2.5, 3])

    # tai san dam bao
    taisan['yeu'] = fuzz.trapmf(taisan.universe, [0, 0, 0.5, 1])
    taisan['trung binh'] = fuzz.trapmf(taisan.universe, [0.5, 1, 1.5, 2])
    taisan['manh'] = fuzz.trapmf(taisan.universe, [1.5, 2, 2.5, 3])

    # muc tin dung
    tindung['yeu'] = fuzz.trapmf(tindung.universe, [0, 0, 0.5, 1])
    tindung['trung binh'] = fuzz.trapmf(tindung.universe, [0.5, 1, 1.5, 2])
    tindung['manh'] = fuzz.trapmf(tindung.universe, [1.5, 2, 2.5, 3])

    # nhan khau 1
    nhankhau1['yeu'] = fuzz.trapmf(nhankhau1.universe, [0, 0, 0.5, 1])
    nhankhau1['trung binh'] = fuzz.trapmf(nhankhau1.universe, [0.5, 1, 1.5, 2])
    nhankhau1['manh'] = fuzz.trapmf(nhankhau1.universe, [1.5, 2, 2.5, 3])

    # tai chinh 1
    taichinh1['yeu'] = fuzz.trapmf(taichinh1.universe, [0, 0, 0.5, 1])
    taichinh1['trung binh'] = fuzz.trapmf(taichinh1.universe, [0.5, 1, 1.5, 2])
    taichinh1['manh'] = fuzz.trapmf(taichinh1.universe, [1.5, 2, 2.5, 3])

    # tai san 1
    taisan1['yeu'] = fuzz.trapmf(taisan1.universe, [0, 0, 0.5, 1])
    taisan1['trung binh'] = fuzz.trapmf(taisan1.universe, [0.5, 1, 1.5, 2])
    taisan1['manh'] = fuzz.trapmf(taisan1.universe, [1.5, 2, 2.5, 3])

    # muc tin dung 1
    tindung1['yeu'] = fuzz.trapmf(tindung1.universe, [0, 0, 0.5, 1])
    tindung1['trung binh'] = fuzz.trapmf(tindung1.universe, [0.5, 1, 1.5, 2])
    tindung1['manh'] = fuzz.trapmf(tindung1.universe, [1.5, 2, 2.5, 3])

    # luat nhan khau hoc
    rule1 = ctrl.Rule(age['tre'] & academic_lv['thap'] & marital_stt['doc than'] & children['it'], nhankhau['yeu'])
    rule2 = ctrl.Rule(age['tre'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['it'],nhankhau['trung binh'])
    rule3 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['doc than'] & children['it'], nhankhau['yeu'])
    rule4 = ctrl.Rule(age['trung nien'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['it'], nhankhau['trung binh'])
    rule5 = ctrl.Rule(age['gia'] & academic_lv['thap'] & marital_stt['doc than'] & children['it'], nhankhau['yeu'])
    rule6 = ctrl.Rule(age['gia'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['it'], nhankhau['trung binh'])
    rule7 = ctrl.Rule(age['tre'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['it'], nhankhau['yeu'])
    rule8 = ctrl.Rule(age['tre'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['it'], nhankhau['trung binh'])
    rule9 = ctrl.Rule(age['tre'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['it'], nhankhau['manh'])
    rule10 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['it'], nhankhau['yeu'])
    rule11 = ctrl.Rule(age['trung nien'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['it'], nhankhau['trung binh'])
    rule12 = ctrl.Rule(age['trung nien'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['it'], nhankhau['manh'])
    rule13 = ctrl.Rule(age['gia'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['it'], nhankhau['yeu'])
    rule14 = ctrl.Rule(age['gia'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['it'], nhankhau['trung binh'])
    rule15 = ctrl.Rule(age['gia'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['it'], nhankhau['manh'])
    rule16 = ctrl.Rule(age['tre'] & (academic_lv['thap'] | academic_lv['trung binh']) & marital_stt['doc than'] & children['vua'], nhankhau['yeu'])
    rule17 = ctrl.Rule(age['tre'] & academic_lv['cao'] & marital_stt['doc than'] & children['vua'], nhankhau['trung binh'])
    rule18 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['doc than'] & children['vua'], nhankhau['yeu'])
    rule19 = ctrl.Rule(age['trung nien'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['vua'], nhankhau['trung binh'])
    rule20 = ctrl.Rule(age['gia'] & academic_lv['thap'] & marital_stt['doc than'] & children['vua'], nhankhau['yeu'])
    rule21 = ctrl.Rule(age['gia'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['vua'], nhankhau['trung binh'])
    rule22 = ctrl.Rule(age['tre'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['yeu'])
    rule23 = ctrl.Rule(age['tre'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['trung binh'])
    rule24 = ctrl.Rule(age['tre'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['manh'])
    rule25 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['yeu'])
    rule26 = ctrl.Rule(age['trung nien'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['trung binh'])
    rule27 = ctrl.Rule(age['trung nien'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['manh'])
    rule28 = ctrl.Rule(age['gia'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['yeu'])
    rule29 = ctrl.Rule(age['gia'] & academic_lv['trung binh'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['trung binh'])
    rule30 = ctrl.Rule(age['gia'] & academic_lv['cao'] & marital_stt['co gia dinh'] & children['vua'], nhankhau['manh'])
    rule31 = ctrl.Rule(age['tre'] & (academic_lv['thap'] | academic_lv['trung binh']) & marital_stt['doc than'] & children['nhieu'], nhankhau['yeu'])
    rule32 = ctrl.Rule(age['tre'] & academic_lv['cao'] & marital_stt['doc than'] & children['nhieu'], nhankhau['trung binh'])
    rule33 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['doc than'] & children['nhieu'], nhankhau['yeu'])
    rule34 = ctrl.Rule(age['trung nien'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['doc than'] & children['nhieu'], nhankhau['trung binh'])
    rule35 = ctrl.Rule(age['gia'] & (academic_lv['thap'] | academic_lv['trung binh']) & marital_stt['doc than'] & children['nhieu'], nhankhau['yeu'])
    rule36 = ctrl.Rule(age['gia'] & academic_lv['cao'] & marital_stt['doc than'] & children['nhieu'], nhankhau['trung binh'])
    rule37 = ctrl.Rule(age['tre'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['yeu'])
    rule38 = ctrl.Rule(age['tre'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['trung binh'])
    rule39 = ctrl.Rule(age['trung nien'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['yeu'])
    rule40 = ctrl.Rule(age['trung nien'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['trung binh'])
    rule41 = ctrl.Rule(age['gia'] & academic_lv['thap'] & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['yeu'])
    rule42 = ctrl.Rule(age['gia'] & (academic_lv['trung binh'] | academic_lv['cao']) & marital_stt['co gia dinh'] & children['nhieu'], nhankhau['trung binh'])

    credit_scoring_nhankhau = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                                  rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
                                                  rule19, rule20,
                                                  rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28,
                                                  rule29, rule30,
                                                  rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38,
                                                  rule39, rule40,
                                                  rule41, rule42])
    credit_scoring_nhankhau_sim = ctrl.ControlSystemSimulation(credit_scoring_nhankhau)
    credit_scoring_nhankhau_sim.input['tuoi'] = float(age_get)
    credit_scoring_nhankhau_sim.input['trinh_do_hoc_van'] = float(academic_lv_get)
    credit_scoring_nhankhau_sim.input['tinh_trang_hon_nhan'] = float(marital_stt_get)
    credit_scoring_nhankhau_sim.input['so_con'] = float(children_get)
    credit_scoring_nhankhau_sim.compute()
    kqnhankhauhoc = credit_scoring_nhankhau_sim.output['nhan_khau_hoc']
    # nhankhau.view(sim=credit_scoring_nhankhau_sim)

    # luat tai chinh
    rule43 = ctrl.Rule(month_income['thap'] & (seniority['ngan'] | seniority['trung binh']) & employment_contract['thoi vu'], taichinh['yeu'])
    rule44 = ctrl.Rule(month_income['thap'] & seniority['dai'] & employment_contract['thoi vu'], taichinh['trung binh'])
    rule45 = ctrl.Rule(month_income['thap'] & (seniority['ngan'] | seniority['trung binh']) & employment_contract['co thoi han'], taichinh['yeu'])
    rule46 = ctrl.Rule(month_income['thap'] & seniority['dai'] & employment_contract['co thoi han'], taichinh['trung binh'])
    rule47 = ctrl.Rule(month_income['thap'] & seniority['ngan'] & employment_contract['khong thoi han'], taichinh['yeu'])
    rule48 = ctrl.Rule(month_income['thap'] & (seniority['trung binh'] | seniority['dai']) & employment_contract['khong thoi han'], taichinh['trung binh'])
    rule49 = ctrl.Rule(month_income['trung binh'] & seniority['ngan'] & employment_contract['thoi vu'], taichinh['yeu'])
    rule50 = ctrl.Rule(month_income['trung binh'] & (seniority['trung binh'] | seniority['dai']) & employment_contract['thoi vu'], taichinh['trung binh'])
    rule51 = ctrl.Rule(month_income['trung binh'] & seniority['ngan'] & employment_contract['co thoi han'], taichinh['yeu'])
    rule52 = ctrl.Rule(month_income['trung binh'] & (seniority['trung binh'] | seniority['dai']) & employment_contract['co thoi han'], taichinh['trung binh'])
    rule53 = ctrl.Rule(month_income['trung binh'] & (seniority['ngan'] | seniority['trung binh']) & employment_contract['khong thoi han'], taichinh['trung binh'])
    rule54 = ctrl.Rule(month_income['trung binh'] & seniority['dai'] & employment_contract['khong thoi han'], taichinh['manh'])
    rule55 = ctrl.Rule(month_income['cao'] & (seniority['ngan'] | seniority['trung binh']) & employment_contract['thoi vu'], taichinh['trung binh'])
    rule56 = ctrl.Rule(month_income['cao'] & seniority['dai'] & employment_contract['thoi vu'], taichinh['manh'])
    rule57 = ctrl.Rule(month_income['cao'] & seniority['ngan'] & employment_contract['co thoi han'], taichinh['trung binh'])
    rule58 = ctrl.Rule(month_income['cao'] & (seniority['trung binh'] | seniority['dai']) & employment_contract['co thoi han'], taichinh['manh'])
    rule59 = ctrl.Rule(month_income['cao'] & (seniority['ngan'] | seniority['trung binh'] | seniority['dai']) & employment_contract['khong thoi han'], taichinh['manh'])

    credit_scoring_taichinh = ctrl.ControlSystem([rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
                                                  rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58,
                                                  rule59])
    credit_scoring_taichinh_sim = ctrl.ControlSystemSimulation(credit_scoring_taichinh)
    credit_scoring_taichinh_sim.input['thu_nhap_hang_thang'] = float(month_income_get)
    credit_scoring_taichinh_sim.input['tham_nien'] = float(seniority_get)
    credit_scoring_taichinh_sim.input['loai_hop_dong'] = float(employment_contract_get)
    credit_scoring_taichinh_sim.compute()
    kqtaichinh = credit_scoring_taichinh_sim.output['tai_chinh']
    # taichinh.view(sim=credit_scoring_taichinh_sim)

    # luat tai san
    rule60 = ctrl.Rule(bike_property_value['re'] & (house_property_value['thap'] | house_property_value['trung binh']) & other_property_value['thap'], taisan['yeu'])
    rule61 = ctrl.Rule(bike_property_value['re'] & house_property_value['cao'] & other_property_value['thap'], taisan['trung binh'])
    rule62 = ctrl.Rule(bike_property_value['re'] & (house_property_value['thap'] | house_property_value['trung binh']) & other_property_value['trung binh'], taisan['yeu'])
    rule63 = ctrl.Rule(bike_property_value['re'] & house_property_value['cao'] & other_property_value['trung binh'], taisan['manh'])
    rule64 = ctrl.Rule(bike_property_value['re'] & house_property_value['thap'] & other_property_value['cao'], taisan['yeu'])
    rule65 = ctrl.Rule(bike_property_value['re'] & house_property_value['trung binh'] & other_property_value['cao'], taisan['trung binh'])
    rule66 = ctrl.Rule(bike_property_value['re'] & house_property_value['cao'] & other_property_value['cao'], taisan['manh'])
    rule67 = ctrl.Rule(bike_property_value['vua'] & house_property_value['thap'] & other_property_value['thap'], taisan['yeu'])
    rule68 = ctrl.Rule(bike_property_value['vua'] & house_property_value['trung binh'] & other_property_value['thap'], taisan['trung binh'])
    rule69 = ctrl.Rule(bike_property_value['vua'] & house_property_value['cao'] & other_property_value['thap'], taisan['manh'])
    rule70 = ctrl.Rule(bike_property_value['vua'] & (house_property_value['thap'] | house_property_value['trung binh']) & other_property_value['trung binh'], taisan['trung binh'])
    rule71 = ctrl.Rule(bike_property_value['vua'] & house_property_value['cao'] & other_property_value['trung binh'], taisan['manh'])
    rule72 = ctrl.Rule(bike_property_value['vua'] & (house_property_value['thap'] | house_property_value['trung binh']) & other_property_value['cao'], taisan['trung binh'])
    rule73 = ctrl.Rule(bike_property_value['vua'] & house_property_value['cao'] & other_property_value['cao'], taisan['manh'])
    rule74 = ctrl.Rule(bike_property_value['dat'] & house_property_value['thap'] & other_property_value['thap'], taisan['yeu'])
    rule75 = ctrl.Rule(bike_property_value['dat'] & house_property_value['trung binh'] & other_property_value['thap'], taisan['trung binh'])
    rule76 = ctrl.Rule(bike_property_value['dat'] & house_property_value['cao'] & other_property_value['thap'], taisan['manh'])
    rule77 = ctrl.Rule(bike_property_value['dat'] & (house_property_value['thap'] | house_property_value['trung binh']) & other_property_value['trung binh'], taisan['trung binh'])
    rule78 = ctrl.Rule(bike_property_value['dat'] & house_property_value['cao'] & other_property_value['trung binh'], taisan['manh'])
    rule79 = ctrl.Rule(bike_property_value['dat'] & house_property_value['thap'] & other_property_value['cao'], taisan['trung binh'])
    rule80 = ctrl.Rule(bike_property_value['dat'] & (house_property_value['trung binh'] | house_property_value['cao']) & other_property_value['cao'], taisan['manh'])

    credit_scoring_taisan = ctrl.ControlSystem(
        [rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69,
         rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80])
    credit_scoring_taisan_sim = ctrl.ControlSystemSimulation(credit_scoring_taisan)
    credit_scoring_taisan_sim.input['gia_tri_tai_san_phuong_tien'] = float(bike_property_value_get)
    credit_scoring_taisan_sim.input['gia_tri_tai_san_nha_o'] = float(house_property_value_get)
    credit_scoring_taisan_sim.input['gia_tri_tai_san_khac'] = float(other_property_value_get)
    credit_scoring_taisan_sim.compute()
    kqtaisan = credit_scoring_taisan_sim.output['tai_san_dam_bao']
    # taisan.view(sim=credit_scoring_taisan_sim)

    # luat muc tin dung
    rule81 = ctrl.Rule(owned_debt['khong no'] & finished_transaction['yeu'], tindung['yeu'])
    rule82 = ctrl.Rule(owned_debt['khong no'] & finished_transaction['trung binh'], tindung['trung binh'])
    rule83 = ctrl.Rule(owned_debt['khong no'] & finished_transaction['manh'], tindung['manh'])
    rule84 = ctrl.Rule(owned_debt['no it'] & finished_transaction['yeu'], tindung['yeu'])
    rule85 = ctrl.Rule(owned_debt['no it'] & finished_transaction['trung binh'], tindung['trung binh'])
    rule86 = ctrl.Rule(owned_debt['no it'] & finished_transaction['manh'], tindung['manh'])
    rule87 = ctrl.Rule(owned_debt['no nhieu'] & finished_transaction['yeu'], tindung['yeu'])
    rule88 = ctrl.Rule(owned_debt['no nhieu'] & finished_transaction['trung binh'], tindung['yeu'])
    rule89 = ctrl.Rule(owned_debt['no nhieu'] & finished_transaction['manh'], tindung['trung binh'])

    credit_scoring_tindung = ctrl.ControlSystem([rule81, rule82, rule83, rule84, rule85, rule86,
                                                 rule87, rule88, rule89])
    credit_scoring_tindung_sim = ctrl.ControlSystemSimulation(credit_scoring_tindung)
    credit_scoring_tindung_sim.input['khoan_no_hien_co'] = float(owned_debt_get)
    credit_scoring_tindung_sim.input['giao_dich_da_hoan_tat'] = float(finished_transaction_get)
    credit_scoring_tindung_sim.compute()
    kqtindung = credit_scoring_tindung_sim.output['muc_tin_dung']
    # tindung.view(sim=credit_scoring_tindung_sim)

    # Luat xep hang tin dung
    rule90 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['yeu'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro cao'])
    rule91 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['yeu'] & taisan1['trung binh'] & (tindung1['yeu'] | tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro cao'])
    rule92 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['yeu'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule93 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['yeu'] & taisan1['manh'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro trung binh'])
    rule94 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro cao'])
    rule95 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['trung binh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro cao'])
    rule96 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro trung binh'])
    rule97 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule98 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['manh'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule99 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['trung binh'] & taisan1['manh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule100 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['yeu'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule101 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['yeu'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro trung binh'])
    rule102 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['trung binh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro trung binh'])
    rule103 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule104 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro trung binh'])
    rule105 = ctrl.Rule((nhankhau1['yeu'] & taichinh1['manh'] & taisan1['manh'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro thap'])
    rule106 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro cao'])
    rule107 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['trung binh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro cao'])
    rule108 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro trung binh'])
    rule109 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule110 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['manh'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule111 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['yeu'] & taisan1['manh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule112 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro cao'])
    rule113 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['yeu'] & tindung1['manh']), over_rated['rui ro trung binh'])
    rule114 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['trung binh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule115 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['trung binh'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule116 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule117 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['manh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro trung binh'])
    rule118 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['trung binh'] & taisan1['manh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule119 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['yeu'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule120 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['yeu'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro trung binh'])
    rule121 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['trung binh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule122 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['trung binh'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule123 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule124 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro trung binh'])
    rule125 = ctrl.Rule((nhankhau1['trung binh'] & taichinh1['manh'] & taisan1['manh'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro thap'])
    rule126 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro cao'])
    rule127 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['yeu'] & tindung1['manh']), over_rated['rui ro trung binh'])
    rule128 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['trung binh'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule129 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['trung binh'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule130 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule131 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['manh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro trung binh'])
    rule132 = ctrl.Rule((nhankhau1['manh'] & taichinh1['yeu'] & taisan1['manh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule133 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['yeu'] & tindung1['yeu']), over_rated['rui ro cao'])
    rule134 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['yeu'] & tindung1['trung binh']), over_rated['rui ro trung binh'])
    rule135 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['yeu'] & tindung1['manh']), over_rated['rui ro thap'])
    rule136 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['trung binh'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro trung binh'])
    rule137 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['trung binh'] & tindung1['manh']), over_rated['rui ro thap'])
    rule138 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['manh'] & tindung1['yeu']), over_rated['rui ro trung binh'])
    rule139 = ctrl.Rule((nhankhau1['manh'] & taichinh1['trung binh'] & taisan1['manh'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro thap'])
    rule140 = ctrl.Rule((nhankhau1['manh'] & taichinh1['manh'] & taisan1['yeu'] & (tindung1['yeu'] | tindung1['trung binh'])), over_rated['rui ro trung binh'])
    rule141 = ctrl.Rule((nhankhau1['manh'] & taichinh1['manh'] & taisan1['yeu'] & tindung1['manh']), over_rated['rui ro thap'])
    rule142 = ctrl.Rule((nhankhau1['manh'] & taichinh1['manh'] & taisan1['trung binh'] & tindung1['yeu']), over_rated['rui ro trung binh'])
    rule143 = ctrl.Rule((nhankhau1['manh'] & taichinh1['manh'] & taisan1['trung binh'] & (tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro thap'])
    rule144 = ctrl.Rule((nhankhau1['manh'] & taichinh1['manh'] & taisan1['manh'] & (tindung1['yeu'] | tindung1['trung binh'] | tindung1['manh'])), over_rated['rui ro thap'])

    credit_scoring_rules = ctrl.ControlSystem([rule90, rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99,
                                             rule100, rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109,
                                             rule110, rule111, rule112, rule113, rule114, rule115, rule116, rule117, rule118, rule119,
                                             rule120, rule121, rule122, rule123, rule124, rule125, rule126, rule127, rule128, rule129,
                                             rule130, rule131, rule132, rule133, rule134, rule135, rule136, rule137, rule138, rule139,
                                             rule140, rule141, rule142, rule143, rule144])
    credit_scoring_rules_sim = ctrl.ControlSystemSimulation(credit_scoring_rules)
    credit_scoring_rules_sim.input['nhan_khau_hoc1'] = float(kqnhankhauhoc)
    credit_scoring_rules_sim.input['tai_chinh1'] = float(kqtaichinh)
    credit_scoring_rules_sim.input['tai_san_dam_bao1'] = float(kqtaisan)
    credit_scoring_rules_sim.input['muc_tin_dung1'] = float(kqtindung)
    credit_scoring_rules_sim.compute()
    ketqua = credit_scoring_rules_sim.output['ket_qua']
    # over_rated.view(sim=credit_scoring_rules_sim)

    messagebox.showinfo("Thông báo", f"Nhân khẩu: {kqnhankhauhoc}\nTài chính: {kqtaichinh}\nTài sản: {kqtaisan}\nMức tín dụng: {kqtindung}\nKết quả xếp hạng tín dụng: {ketqua}")

root = Tk()
root.title("KLTN")
root.geometry("500x650")
Label(root, text="ID").place(x=10, y=10)
Button(root, text="Search", command=searchdata ,height = 1, width = 13).place(x=160, y=40)
Button(root, text="Credit", command=credit ,height = 1, width = 13).place(x=300, y=40)
Label(root, text="Name").place(x=10, y=80)
Label(root, text="Age").place(x=10, y=120)
Label(root, text="Academic_lv").place(x=10, y=160)
Label(root, text="Marital_stt").place(x=10, y=200)
Label(root, text="Children").place(x=10, y=240)
Label(root, text="Month_income").place(x=10, y=280)
Label(root, text="Seniority").place(x=10, y=320)
Label(root, text="Employment_contract").place(x=10, y=360)
Label(root, text="Bike_property_value").place(x=10, y=400)
Label(root, text="House_property_value").place(x=10, y=440)
Label(root, text="Other_property_value").place(x=10, y=480)
Label(root, text="Owned_debt").place(x=10, y=520)
Label(root, text="Finished_transaction").place(x=10, y=560)
Label(root, text="Nguyễn Văn Lượng\nĐào Ngọc Sang").place(x=380, y=590)

e1 = Entry(root)
e1.place(x=160, y=10)
e2 = Entry(root)
e2.place(x=160, y=80)
e3 = Entry(root)
e3.place(x=160, y=120)
e4 = Entry(root)
e4.place(x=160, y=160)
e5 = Entry(root)
e5.place(x=160, y=200)
e6 = Entry(root)
e6.place(x=160, y=240)
e7 = Entry(root)
e7.place(x=160, y=280)
e8 = Entry(root)
e8.place(x=160, y=320)
e9 = Entry(root)
e9.place(x=160, y=360)
e10 = Entry(root)
e10.place(x=160, y=400)
e11 = Entry(root)
e11.place(x=160, y=440)
e12 = Entry(root)
e12.place(x=160, y=480)
e13 = Entry(root)
e13.place(x=160, y=520)
e14 = Entry(root)
e14.place(x=160, y=560)

root.mainloop()