# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import local_strage
import json
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://localhost:1337/')
storage = local_strage.LocalStorage(driver)

name = "room_moyo_kae"

# ガントへデータからエクセルへ

task = storage["task"]
task =json.loads(task)
df_task = pd.DataFrame(task)
df_dic = df_task[["id"]].copy()
df_dic["sin_id"] = f"{name}_" + (df_dic.index + 1).astype("str")
df_dic = df_dic.astype("str")
dic = dict(df_dic.set_index("id")["sin_id"])
df_task = df_task.astype("str")
df_task["id"] = df_task["id"].map(dic)
df_task["parent"] = df_task["parent"].map(dic)
df_task.to_csv(f"data/{name}.csv",index=False)
df_task.to_excel(f"data/{name}.xlsx",index=False)

# df_taskを編集

# ! code .

# 編集結果を取得

# df_task_edit = pd.read_csv("df_task.csv")
df_table = pd.read_excel(f"data/{name}.xlsx")
df_table["kind_task"] = df_table["kind_task"].astype("str")

# データを戻す

out_json = df_table.to_json(orient='records')
storage.set("task", out_json)
driver.refresh()

# 完了したら閉じる

driver.quit()

# 消す

storage.clear()


