#!/usr/local/bin/python3
#
#	Mastodon用トゥートBOT
#	サンプルソース
#

from mastodon import Mastodon
import random
import sys
import io

#setting
url = 'URL'						#インスタンスのURL
dir = 'DIR'						#BOT本体が置いてあるURL
client_file =	'client.dat'	#client
token_file =	'token.dat'		#token
bot_txt = 		'bot_toot.dat'	#ランダムトゥート用テキスト
before_txt = 	'tmp.dat'		#重複チェック用
txt_enc =		'utf-8'			#テキストエンコード
txt_file_enc =	'utf-8_sig'

#text encode
sys.stdin =  io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
print("Content-type: text/html; charset=UTF-8\n\n")

#テキストファイル読み込み
f = open(bot_txt,'r',encoding="utf-8_sig")
lines = [s.strip() for s in f.readlines()]
num_lines = sum(1 for line in lines)
f.close()

#前回のトゥートを読み込み
f = open(before_txt, 'r', encoding="utf-8")
dup_txt = f.read()
f.close()

#ランダム選択
random_line = random.randrange(1, num_lines, 1)
while(dup_txt == lines[random_line]):
	random_line = random.randrange(1, num_lines, 1)

print(random_line, lines[random_line])

#トゥートを書き込み（二重投稿対策）
f = open(before_txt, 'w', encoding="utf-8_sig")
f.write(lines[random_line])
f.close()

#login
def mastodon_login():
	mastodon = Mastodon(
		client_id=client_file,
		access_token=token_file,
		api_base_url=url
	)

def main():

	mastodon_login()

	#toot
	mastodon.toot(lines[random_line])

if __name__ == '__main__':
    main()
