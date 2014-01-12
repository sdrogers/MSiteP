import os

def populate():
	with open('mplister/all.MPS') as f:
		content = f.readlines()
	for c in content:
		comps = c.split('\t')
		p = addparty(comps[3].rstrip())
		name = comps[1]
		url = name.replace(', ','_')
		addmsp(comps[1],p,comps[2],url)

def addparty(name):
	p = Party.objects.get_or_create(name = name)[0]
	return p
def addmsp(name,party,constituency,url):
	m = MSP.objects.get_or_create(name = name,party = party,constituency=constituency,url=url)[0]
	return m



if __name__ == '__main__':
    print "Starting mplister population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toy_project.settings')
    from mplister.models import Party, MSP
    populate()