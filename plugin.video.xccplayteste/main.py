<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addons>
<addon id="plugin.video.xccplayteste" version="1.0.0" name="XCC Play!" provider-name="Carl Henriyx">
    <requires>
        <import addon="xbmc.python" version="3.0.0"/>
        <import addon="script.module.requests"/>
    </requires>
    <extension point="xbmc.python.pluginsource" library="main.py">
        <provides>video</provides>
    </extension>
    <extension point="xbmc.addon.metadata">
        <summary lang="pt">Meu Addon de Filmes M3U</summary>
        <description lang="pt">Addon com lista M3U integrada.</description>
        <platform>all</platform>
        <assets>
            <icon>icon.png</icon>
            <fanart>fanart.jpg</fanart>
        </assets>
    </extension>
</addon>
</addons>

