from PIL import Image
import os
import datetime
import img2pdf


if __name__ == '__main__':
    pdfFileName = "hoge.pdf"  # 作成するpdfファイル名
    path = "hoge"  # 画像ファイルが入っているディレクトリ
    ext_p = ".png"
    ext_j = ".jpg"
    save_directory = "output_pdf" + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    os.mkdir(save_directory)

    with open(save_directory + "/" + pdfFileName, "wb") as f:
        imageList = []
        for item in os.listdir(path):
            if item.endswith(ext_p):
                image = Image.open(path + "/" + item)
                image = image.convert('RGB')
                image.save(save_directory + "/" + item[:-3] + 'jpg')
                imageList = imageList + [save_directory + "/" + item[:-3] + 'jpg']
            elif item.endswith(ext_j):
                image = Image.open(path + "/" + item)
                image = image.convert('RGB')
                imageList = imageList + [path + "/" + item]
            imageList.sort()

        f.write(img2pdf.convert(imageList))

    # 余分に作成したjpgファイルの削除
    # 残しておきたい場合はコメントアウトする
    for i in imageList:
        os.remove(i)
