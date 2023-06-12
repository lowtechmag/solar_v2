---
title: "Energie"
date: ""
summary: "Deze website draait op [zonne-energie](/nl/about/the-solar-website). De server staat opgesteld in Barcelona en gaat offline gedurende langere periodes van slecht weer. Deze pagina geeft \"live\" informatie weer over de productie van zonne-energie, de energieopslag, en het energieverbruik van de website."
slug: "power"
lang: "nl"
authors: ["" ]
categories: [""]
tags: []
featured_image: "solar-powered-server-weather-2.png"
---

## Energieproductie

Dit is de lokale weersverwachting voor de komende dagen (dagelijkse update):
<p class="forecast">
</p>

Dit weerbericht [powered by BrightSky](https://brightsky.dev/). 

## Energievraag

Dit zijn de data die door de server worden geregistreerd:
<dl id="server">
</dl>

(* gemiddelde per 15 minuten)

## Energieopslag

De achtergrond van deze website is een batterijmeter, die aangeeft over hoeveel energieopslag de zonne-installatie beschikt. Sinds 12 januari 2020 draait de website op haar huidige configuratie: een zonnepaneel van 30W en een loodzuurbatterij van 168 watt-uur.

De batterijmeter toont het voltage van de batterij. Bijvoorbeeld een opslagcapaciteit van 68% komt overeen met een voltage van 12.68 volt. Het voltage komt echter niet altijd overeen met de capaciteit van de energieopslag. 

De elektrische lading van de server (die het voltage van de batterij verlaagt) kan makkelijk worden ingecalculeerd omdat het elektriciteitsverbruik van de server vrijwel constant is. Maar de zonnestraling (die het voltage van de batterij doet toenemen) is daarentegen heel veranderlijk. 

Tijdens de nacht reflecteert het voltage accuraat de opslagcapaciteit van de batterij: de batterijmeter is dan heel precies en zal langzaam zakken. Overdag weerspiegelt de batterijmeter de lokale weersomstandigheden. Als het zonnepaneel volle zon ontvangt, stijgt het voltage boven de 13 volt en wordt de hele website in het geel gekleurd. Als het bewolkt genoeg is, dan zakt de batterijmeter en wordt de blauwe achtergrond onthuld. Als het voltage van de batterij onder de 12V zakt, en de hele pagina in het blauw is gekleurd, sluit de zonneregelaar het systeem af en gaat de website offline. Ze komt weer online als de zon opnieuw schijnt. 

{{% figure src="solar-powered-server-weather-2.png" %}} De toegankelijkheid van deze website hangt af van het weer in Barcelona, Spanje. {{% /figure %}}
