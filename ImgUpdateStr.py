# -*- coding: utf-8 -*-
# @file : ImgUpdateStr.py
# @Time : 2021-09-02 10:00
# @Author : housongcheng

from PIL import Image, ImageDraw, ImageFont

def ImgDealWith(source_path, add_str, save_path):
    oriImg = Image.open(source_path)
    draw = ImageDraw.Draw(oriImg)
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)
    w, h = font.getsize(add_str)
    draw.text(((700 - w) / 2, 300), add_str, fill='black', font=font)
    oriImg.show()
    oriImg.save(save_path)

if __name__ == '__main__':
    # 预处理图片路径
    source_path = 'img_before.jpg'
    # 处理完图片保存路径
    save_path = 'img_after.png'
    # 添加图片上的文字信息
    add_str = "add_strs"
    ImgDealWith(source_path, add_str, save_path)
    
