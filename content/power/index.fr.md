---
title: "Power"
date: ""
summary: "This website runs on a [solar powered server](/fr/about/the-solar-website) located in Barcelona, and will go off-line during longer periods of bad weather. This page shows live data relating to power supply, power demand, and energy storage."
slug: "power"
lang: "fr"
authors: ["" ]
categories: [""]
tags: []
featured_image: "solar-powered-server-weather-2.png"
---

## Power supply

This is a forecast for the coming days, updated daily:
<p class="forecast">
</p>

This weather forecast is [powered by BrightSky](https://brightsky.dev/). 

## Power demand

These are live power statistics of the solar powered server:
<dl id="server">
</dl>

(* load average per 15 minutes)

## Battery meter

The background of this website is a battery meter, designed to always display the relationship of the energy powering the website and the visitor traffic consuming it. Since 12 January 2020, the website runs on a 30W solar panel and a 168 Wh lead-acid battery.

We also installed a new battery meter, which simply represents the voltage of our battery. For example, a storage capacity of 68% converts to 12.68V, and the other way around. Showing a correct representation of the storage capacity requires calibration and algorithms in relation to a specific battery. This is troublesome, because we [keep experimenting with different sizes of batteries and solar panels]({{< ref "/posts/how-sustainable-is-a-solar-powered-website" >}}) to find the optimal balance between uptime and sustainability.

The voltage reading is the "naked" data on which each battery meter relies to display a percentage. The voltage of the battery doesn't always correlate with the energy storage capacity -- it's also influenced by the electric load (which lowers the voltage) and the solar insolation (which increases the voltage). 

Because our load (the server) has a rather constant power use, during the day our battery meter reflects the local solar conditions. If the panel receives full sun, the voltage will most likely raise above 13V, colouring the whole website in yellow. However, if it's cloudy enough, the battery meter will decrease and the blue background is revealed. 

Because our load is constant, during the night the battery meter reflects the storage capacity of the battery accurately. When the voltage of the battery drops below 12V, and the whole page is coloured in blue, the solar charge controller shuts down the system and the website goes offline. 

{{% figure src="solar-powered-server-weather-2.png" %}} The accessibility of this website depends on the weather in Barcelona, Spain. {{% /figure %}}
