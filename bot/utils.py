import requests

def get_questions(tags, title):
	r_tags = ";".join(tags)
	print(r_tags)
	url = "https://api.stackexchange.com/2.2/search/advanced"
	# headers = 
	params = {
		'order':'desc',
		'sort' : 'votes',
		'site' : 'stackoverflow',
		'pagesize' : 3,
		# 'intitle' : '',
		'q': title
	}
	if len(tags) > 0:
		params.update({'tagged' : r_tags})
	print(params)
	r = requests.get(url, params=params)
	questions = r.json()
	output = []
	for question in questions['items']:
		output.append(question['title'])
		output.append(question['link'])
		output.append("\n")
	output = "\n".join(output)
	return(output)

# print(get_questions(['python','django'],'CORS'))
# print(get_questions(['react','css'],'alignment'))