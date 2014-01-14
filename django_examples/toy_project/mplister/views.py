# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mplister.models import Party, MSP

def index(request):
	context = RequestContext(request)
	party_list = Party.objects.order_by('name')
	context_dict = {'parties': party_list}
	msp_list = MSP.objects.order_by('party')
	context_dict['MSP'] = msp_list
	return render_to_response('mplister/index.html', context_dict, context)

def party(request,party_name):
	context = RequestContext(request)
	context_dict = {'party_name': party_name}
	try:
		p = Party.objects.get(name__iexact = party_name)
		msps = MSP.objects.filter(party = p)
		context_dict['msps'] = msps
		context_dict['party'] = p
	except:
		pass

	return render_to_response('mplister/party.html',context_dict,context)

def msp(request,msp_name_url):
	context = RequestContext(request)
	context_dict = {'msp_name_url':msp_name_url}
	try:
		m = MSP.objects.get(url__iexact = msp_name_url)		
		context_dict['msp_name'] = m.name
		context_dict['party'] = m.party
		context_dict['constituency'] = m.constituency
		context_dict['notes'] = m.notes


	except:
		pass

	return render_to_response('mplister/msp.html',context_dict,context)

def random(request):
	context = RequestContext(request)
	m = MSP.objects.order_by('?')[0]
	context_dict = {'msp_name':m.name}
	context_dict['party'] = m.party
	context_dict['constituency'] = m.constituency
	context_dict['notes'] = m.notes
	return render_to_response('mplister/random.html',context_dict,context)
