from src.utils.request_response import PageFocus

class Main(PageFocus):
    def __init__(self):
        super().__init__()

    def _main(self):
        soup = self.request_page('https://data.bnn.go.id/dataset/jumlah-tahanan-tindak-pidana-narkoba/resource/3b15d71e-24b9-41c7-9bb1-c60598fbdbe8')
        soups = self.request_page('https://data.bnn.go.id/dataset/jumlah-kasus-tindak-pidana-narkoba-berdasarkan-jenis-barang-bukti-peran-dan-provinsi')
        datas2 = self.table(soups)
        datas = self.element(soup, datas2)
        print(datas)


if __name__ == "__main__":
    Main()._main()
