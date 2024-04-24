import time

from datetime import datetime

sekarang = datetime.now()
format_ymd_hms = sekarang.strftime("%Y-%m-%d %H:%M:%S")

class HardCode():
    def __init__(self):
        super().__init__()

    def element(self, soup, datas2):
        datas = {
            'link': 'https://data.bnn.go.id/dataset/jumlah-tahanan-tindak-pidana-narkoba',
            'tag': ['data','bnn','dataset'],
            'domain': 'data.bnn.go.id',
            'title': ''
        }

        title = soup.find(class_='page-heading')
        des = soup.find(class_='prose notes')
        datas.update(
            {
                'title':title.text.strip(),
                'description': des.text.strip()
            }
        )

        datas.update(datas2)

        links = soup.find('a', class_='btn btn-primary resource-url-analytics').get('href')

        file_name_download = links.split('/')[-1]
        file_name_json = f"{des.find('p').text.strip().replace(' ','_').lower()}.json"
        file_name = [
            file_name_json, file_name_download
        ]

        path_data_raw = [
        ]

        path_data_clean = [
        ]

        for name in file_name:
            format = name.split('.')[-1]
            path_data_raw.append(
                f's3://ai-pipeline-statistics/data/data_raw/bnn/Satu Data BNN/Jumlah Tahanan Tindak Pidana Narkoba/{format}/{name}'
            )
            path_data_clean.append(
                f's3://ai-pipeline-statistics/data/data_clean/bnn/Satu Data BNN/Jumlah Tahanan Tindak Pidana Narkoba/{format}/{name}'
            )


        table = soup.find('tbody')
        all_data = []
        for tr in table.find_all('tr'):
            if tr.find('th'):
                all_data.append(
                    {
                        tr.find('th').text.strip().lower().replace(' ','_'):tr.find('td').text.strip()
                    }
                )


        for data in all_data:
            datas.update(data)


        datas.update(
            {
                "file_name":file_name,
                "path_data_raw": path_data_raw,
                "path_data_clean": path_data_clean,
                "crawling_time": format_ymd_hms,
                "crawling_time_epoch": int(time.time())
            }
        )

        return datas



    def table(self, soup):
        datas = {}
        table = soup.find(class_='table table-striped table-bordered table-condensed')
        tbody = table.find('tbody')

        all_data = []

        for tr in (tbody.find_all('tr')):
            if tr.find('th'):
                all_data.append(
                    {
                        tr.find('th').text.strip().lower().replace(' ', '_'): tr.find('td').text.strip()
                    }
                )


        for data in all_data:
            datas.update(data)

        return datas