#!/usr/local/bin/python3
#
#	Mastodon用トゥートBOT
#	サンプルソース
#	その2
#

from mastodon import Mastodon
import random
import sys
import io
from datetime import datetime

# Settings
url = 'URL'						# インスタンスのURL
dir = 'DIR'						# BOT本体が置いてあるURL
client_file =	'client.dat'	# client
token_file =	'token.dat'		# token
bot_txt = 		'bot_toot.dat'	# ランダムトゥート用テキスト
before_txt = 	'tmp.dat'		# 重複チェック用
img_file =		'img_001.jpg'	#
txt_enc =		'utf-8'			# テキストエンコード
txt_file_enc =	'utf-8_sig'		#


# Mastodon Instance Login
def mastodon_login():
    mastodon = Mastodon(
        client_id=client_file,
        access_token=token_file,
        api_base_url=url)

    return (mastodon)


# Mastodon Media Toot
def mastodon_media_post(mastodon,media_file):
    img0 = mastodon.media_post(media_file)
    toot_img = [img0]
    mastodon.status_post(status='', media_ids=toot_img)


#
def mastodon_time_post(mastodon,toot_time):
    get_time = datetime.now()
    now_time = get_time.strftime("%H:%M")
    now_year = get_time.strftime("%Y")
    now_date = get_time.strftime("%m%d")

    if (toot_time == now_time):
        mastodon.toot('OK')


# Main
def main():

    # text encode
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding=txt_enc)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=txt_enc)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=txt_enc)
    print("Content-type: text/html; charset=UTF-8\n\n")

    # テキストファイル読み込み
    f = open(bot_txt, 'r', encoding=txt_file_enc)
    lines = [s.strip() for s in f.readlines()]
    num_lines = sum(1 for line in lines)
    f.close()

    # 前回のトゥートを読み込み
    f = open(before_txt, 'r', encoding=txt_enc)
    dup_txt = f.read()
    f.close()

    # ランダム選択
    random_line = random.randrange(1, num_lines, 1)
    while (dup_txt == lines[random_line]):
        random_line = random.randrange(1, num_lines, 1)

    # トゥートを書き込み（二重投稿対策）
    f = open(before_txt, 'w', encoding=txt_file_enc)
    f.write(lines[random_line])
    f.close()

    mastodon = mastodon_login()


    # mastodon_media_post(mastodon,img_file)		#画像トゥート

	mastodon.toot(lines[random_line])  # テキストトゥート



# おまじない
if __name__ == '__main__':
    main()
