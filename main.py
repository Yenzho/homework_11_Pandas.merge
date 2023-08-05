import pandas as pd

pd.set_option('display.max_columns', None)

def first_exercise():
    df = pd.read_csv("visit_log.csv", sep=';')
    df.loc[df.str.contains("yandex") | df.traffic_source.str.contains("google"), "source_type"] = "organic"
    df.loc[(
                   df.traffic_source.str.contains("paid") | df.traffic_source.str.contains("email")
           ) & (df.region.str.contains("Russia")), "source_type"] = "ad"
    df.loc[(
                   df.traffic_source.str.contains("paid") | df.traffic_source.str.contains("email")
           ) & (df["region"] != "Russia"), "source_type"] = "other"
    df = df.source_type.fillna(df["traffic_source"])
    print(df.head(10))

first_exercise()                    #Первое задание

def second_exercise():
    db = pd.read_csv("URLs.txt")
    db = db[db["url"].str.contains("\\/\\d{8}-", regex=True)]
    print(db.head())

second_exercise()                   #Второе задание

def third_exercise():
    df = pd.read_csv("ml-latest-small\\ratings.csv")
    db = df.userId.value_counts().loc[lambda x: x > 100].reset_index()
    full_base = df.merge(db, on="userId")
    max_time = full_base.groupby("userId")["timestamp"].max().reset_index()
    min_time = full_base.groupby("userId")["timestamp"].min().reset_index()
    min_max_df = max_time.merge(min_time, on="userId")
    min_max_df["life_time"] = min_max_df["timestamp_x"] - min_max_df["timestamp_y"]
    print("Среднее время жизни пользователей, которые выставили более 100 оценок:", round(min_max_df["life_time"].mean()),"секунд")

third_exercise()                       #Третье задание

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

def fourth_exercise():
    rzd_auto = rzd.merge(auto, on='client_id', how="outer")
    three_revenue = rzd_auto.merge(air, on='client_id', how="outer")
    revenue_with_address = three_revenue.merge(client_base, on='client_id', how="outer")
    print(three_revenue.fillna(0)) #если нам нужно привести таблицу в нормальный вид без NaN
    print(revenue_with_address.fillna(0)) #если нам нужно привести таблицу в нормальный вид без NaN

fourth_exercise()                         #Четвертое задание







