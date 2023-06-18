def calculate_population_increase_ratio(first_age, range_age):
    # 基準となる1920年の男性の数、女性の数を求める
    target_population = sum_population(1920, first_age, range_age)
    base_male = target_population['Male']
    base_female = target_population['Female']

    # 各年の計算結果を格納するための空のDataFrameを作成する
    df = pd.DataFrame(index=[], columns=['Year', 'Ratio_Male', 'Ratio_Female'])

    # 人口データに含まれる各年に対して、人口増加率を求める
    for year in population_df['Year'].unique():
        this_year_target_population = sum_population(
            year, first_age, range_age)

        # 男性の人口増加率を求める
        male = this_year_target_population['Male']
        ratio_male = male / base_male

        # 女性の人口増加率を求める
        female = this_year_target_population['Female']
        ratio_female = female / base_female

        # DataFrameに追加するために、それぞれの人口増加率を1つのSeriesにまとめる
        result = pd.Series([year, ratio_male, ratio_female], index=df.columns)
        df = df.append(result, ignore_index=True)

    # データ型を修正する
    df = df.astype(
        {'Year': 'int', 'Ratio_Male': 'float', 'Ratio_Female': 'float'})

    # 計算結果を呼び出し元に戻す
    return
