import pandas as pd


def save_to_excel(raw_data, data_fcfs, data_sjf, file_name, settings):
    # Make data frames
    df = pd.DataFrame(data_fcfs, columns=['Process fcfs', 'Arrival time', 'Duration', 'Time spent in queue'])
    df_settings = pd.DataFrame(settings)
    df2 = pd.DataFrame(data_sjf, columns=['Process lru', 'Arrival time', 'Duration', 'Time spent in queue'])
    df_raw = pd.DataFrame(raw_data, columns=['Process', 'Arrival time', 'Duration'])
    # print lru and fcfs data to the console
    print(df)
    print(df2)
    # Write the processed data to one Excel file
    writer = pd.ExcelWriter(file_name + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', startrow=0, header=True, index=False)
    df2.to_excel(writer, sheet_name='Sheet1', startrow=0, header=True, index=False, startcol=5)
    df_settings.to_excel(writer, sheet_name="Sheet1", startrow=0, header=False, index=False, startcol=10)
    worksheet = writer.sheets["Sheet1"]
    worksheet.set_column(0, 9, 13)
    worksheet.set_column(10, 10, 24)
    writer.close()
    # write the raw data to another Excel file
    writer1 = pd.ExcelWriter(file_name + 'raw_data_gamma.xlsx', engine='xlsxwriter')
    df_raw.to_excel(writer1, sheet_name="Sheet1", startrow=0, header=False, index=False)
    writer1.close()
