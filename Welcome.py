# Databricks notebook source
# MAGIC %md
# MAGIC # Hello

# COMMAND ----------

dbutils.widgets.text("name", "")

# COMMAND ----------

print(f"Hello {dbutils.widgets.get('name')}")

# COMMAND ----------

print("hello")
