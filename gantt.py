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

# ローカルストレージからデータを取得

task = storage["task"]
task =json.loads(task)
df_task = pd.DataFrame(task)
df_task.to_csv("df_task.csv",index=False)

# df_taskを編集

# ! code .

# 編集結果を取得

df_task_edit = pd.read_csv("df_task.csv")
df_task_edit

# データを戻す

out_json = df_task_edit.to_json(orient='records')
storage.set("task", out_json)
driver.refresh()

# 完了したら閉じる

driver.quit()


