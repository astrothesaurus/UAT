# Unified Astronomy Thesaurus v.4.0.0 Release Notes

Version 4.0.0 of the Unified Astronomy Thesaurus consists of a polyhierarchy with 2122 concepts, 11 top concepts, a depth of 11 levels, with 656 related concept links.

Release Date: 12/18/2020

### Overview of Changes
* Five files added to repository:
  * UAT_deprecatedConcepts.rdf - contains all deprecated UAT concepts
  * UAT_skosnotes.rdf - contains definition provenance and "use instead" redirects for deprecated concepts
  * UAT.json - Now expanded to include all concept information, include deprecated concepts
  * UAT_simple.json - Simplified version of the above, only includes parent/child relationships
  * UAT_list.json - Flattened list of UAT concepts, with all information, useful for quick lookups if you know the URI
* One folder added to repository:
  * Previous UAT Versions - contains zipped packages of all previous UAT releases
* Update and expansion of Planetary science branch.
* Added 52 new concepts.
* Deprecated 27 concepts.
* The preferred label of 18 concepts were updated to add context, clarity, and consistency.
* Added or updated AltLabels for 114 concepts, removed AltLabels for 15 concepts.
* Added definitions to 854 concepts, scope notes to 14 concepts, and examples to 9 concepts
* About 40% of UAT concepts now have definitions, more expected in the next release.
* Added 72 new related links, removed 2 related links.
* Resolves Issues in [Milestone ###](https://github.com/astrothesaurus/UAT/milestone/10?closed=1).

### Detailed List of Changes

#### Added 52 new concepts:

| New Concept URI | New Concept PrefLabel |
| --- | --- |
|   http://astrothesaurus.org/uat/2163   |  Flat-spectrum radio quasars  |
|   http://astrothesaurus.org/uat/2164   |  Ultraluminous x-ray sources  |
|   http://astrothesaurus.org/uat/2165   |  Astronomy education  |
|   http://astrothesaurus.org/uat/2166   |  Stellar streams  |
|   http://astrothesaurus.org/uat/2167   |  High angular resolution  |
|   http://astrothesaurus.org/uat/2168   |  AB photometry    |
|   http://astrothesaurus.org/uat/2169   |  Vega photometry  |
|   http://astrothesaurus.org/uat/2170   |  Extreme ultraviolet astronomy    |
|   http://astrothesaurus.org/uat/2171   |  Galaxy spectroscopy  |
|   http://astrothesaurus.org/uat/2172   |  Extrasolar gaseous planets   |
|   http://astrothesaurus.org/uat/2173   |  Planetary dynamics   |
|   http://astrothesaurus.org/uat/2174   |  Volcanism    |
|   http://astrothesaurus.org/uat/2175   |  Tectonics    |
|   http://astrothesaurus.org/uat/2176   |  Post-starburst galaxies  |
|   http://astrothesaurus.org/uat/2177   |  Star-planet interactions     |
|   http://astrothesaurus.org/uat/2178   |  Galactic archaeology     |
|   http://astrothesaurus.org/uat/2179   |  Calibration  |
|   http://astrothesaurus.org/uat/2180   |  Atmospheric clouds   |
|   http://astrothesaurus.org/uat/2181   |  Comet Halley     |
|   http://astrothesaurus.org/uat/2182   |  Eros     |
|   http://astrothesaurus.org/uat/2183   |  Vesta    |
|   http://astrothesaurus.org/uat/2184   |  Planetary climates   |
|   http://astrothesaurus.org/uat/2185   |  Planetary ionospheres    |
|   http://astrothesaurus.org/uat/2186   |  Titan    |
|   http://astrothesaurus.org/uat/2187   |  Triton   |
|   http://astrothesaurus.org/uat/2188   |  Ganymede     |
|   http://astrothesaurus.org/uat/2189   |  Europa   |
|   http://astrothesaurus.org/uat/2190   |  Io   |
|   http://astrothesaurus.org/uat/2191   |  Remote sensing   |
|   http://astrothesaurus.org/uat/2192   |  Aurorae  |
|   http://astrothesaurus.org/uat/2193   |  Lightning    |
|   http://astrothesaurus.org/uat/2194   |  Zodiacal dust bands  |
|   http://astrothesaurus.org/uat/2195   |  Near-sun comets  |
|   http://astrothesaurus.org/uat/2196   |  Sundivers    |
|   http://astrothesaurus.org/uat/2197   |  Sungrazers   |
|   http://astrothesaurus.org/uat/2198   |  Sunskirters  |
|   http://astrothesaurus.org/uat/2199   |  Kracht group     |
|   http://astrothesaurus.org/uat/2200   |  Meyer group  |
|   http://astrothesaurus.org/uat/2201   |  Marsden group    |
|   http://astrothesaurus.org/uat/2202   |  Plutonian satellites     |
|   http://astrothesaurus.org/uat/2203   |  Comet origins    |
|   http://astrothesaurus.org/uat/2204   |  Planetary-disk interactions  |
|   http://astrothesaurus.org/uat/2205   |  Exoplanet migration  |
|   http://astrothesaurus.org/uat/2206   |  Planetary migration  |
|   http://astrothesaurus.org/uat/2207   |  Asteroid satellites  |
|   http://astrothesaurus.org/uat/2208   |  Natural satellite surfaces   |
|   http://astrothesaurus.org/uat/2209   |  Asteroid surfaces    |
|   http://astrothesaurus.org/uat/2210   |  Asteroid dynamics    |
|   http://astrothesaurus.org/uat/2211   |  Asteroid rotation    |
|   http://astrothesaurus.org/uat/2212   |  Natural satellite dynamics   |
|   http://astrothesaurus.org/uat/2213   |  Comet dynamics   |
|   http://astrothesaurus.org/uat/2214   |  Natural satellite atmospheres    |



#### Updated the preferred label of 18 concepts:

| Concept URI | Old PrefLabel | New PrefLabel |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/52     |  Aperiodic comets     |  Interstellar objects     |
|   http://astrothesaurus.org/uat/215    |  Centaurs     |  Centaur group    |
|   http://astrothesaurus.org/uat/258    |  Clouds   |  Earth's clouds   |
|   http://astrothesaurus.org/uat/509    |  Extrasolar gas giants    |  Extrasolar gaseous giant planets     |
|   http://astrothesaurus.org/uat/717    |  Helium weak stars    |  Helium-weak stars    |
|   http://astrothesaurus.org/uat/763    |  Hubble's law     |  Hubble-Lemaitre law  |
|   http://astrothesaurus.org/uat/797    |  Inner planets    |  Solar system terrestrial planets     |
|   http://astrothesaurus.org/uat/860    |  Ionosphere   |  Earth ionosphere     |
|   http://astrothesaurus.org/uat/889    |  Kirkwood gap     |  Kirkwood gaps    |
|   http://astrothesaurus.org/uat/890    |  Kreutz Sungrazers    |  Kreutz group     |
|   http://astrothesaurus.org/uat/997    |  Planetary magnetosphere  |  Planetary magnetospheres     |
|   http://astrothesaurus.org/uat/1191   |  Outer planets    |  Solar system gas giant planets   |
|   http://astrothesaurus.org/uat/1403   |  Ritchey–Chrétien telescopes  |  Ritchey-Chrétien telescopes  |
|   http://astrothesaurus.org/uat/1425   |  Satellite formation  |  Natural satellite formation  |
|   http://astrothesaurus.org/uat/1469   |  Small solar system bodies    |  Small Solar System bodies    |
|   http://astrothesaurus.org/uat/1641   |  Strömgren photometric system     |  Strömgren photometry     |
|   http://astrothesaurus.org/uat/1758   |  Van Allen radiation belt     |  Van Allen radiation belts    |
|   http://astrothesaurus.org/uat/1776   |  Visible astronomy    |  Optical astronomy    |



#### Added 72 new related concept links:

| Concept URI | Concept PrefLabel | Related Concept URI | Related Concept PrefLabel |
| --- | --- | --- | --- |
|   http://astrothesaurus.org/uat/23     |  Alfven waves     |  http://astrothesaurus.org/uat/1964   |  Magnetohydrodynamics     |
|   http://astrothesaurus.org/uat/52     |  Interstellar objects     |  http://astrothesaurus.org/uat/280    |  Comets   |
|   http://astrothesaurus.org/uat/70     |  Asteroid belt    |  http://astrothesaurus.org/uat/2036   |  Main belt asteroids  |
|   http://astrothesaurus.org/uat/72     |  Asteroids    |  http://astrothesaurus.org/uat/1092   |  Near-Earth objects   |
|   http://astrothesaurus.org/uat/72     |  Asteroids    |  http://astrothesaurus.org/uat/2210   |  Asteroid dynamics    |
|   http://astrothesaurus.org/uat/116    |  Atmospheric science  |  http://astrothesaurus.org/uat/1244   |  Planetary atmospheres    |
|   http://astrothesaurus.org/uat/219    |  Ceres    |  http://astrothesaurus.org/uat/2036   |  Main belt asteroids  |
|   http://astrothesaurus.org/uat/280    |  Comets   |  http://astrothesaurus.org/uat/2213   |  Comet dynamics   |
|   http://astrothesaurus.org/uat/280    |  Comets   |  http://astrothesaurus.org/uat/2203   |  Comet origins    |
|   http://astrothesaurus.org/uat/280    |  Comets   |  http://astrothesaurus.org/uat/52     |  Interstellar objects     |
|   http://astrothesaurus.org/uat/280    |  Comets   |  http://astrothesaurus.org/uat/1092   |  Near-Earth objects   |
|   http://astrothesaurus.org/uat/484    |  Exoplanet systems    |  http://astrothesaurus.org/uat/1528   |  Solar system     |
|   http://astrothesaurus.org/uat/493    |  Exoplanet plate tectonics    |  http://astrothesaurus.org/uat/1265   |  Plate tectonics  |
|   http://astrothesaurus.org/uat/509    |  Extrasolar gaseous giant planets     |  http://astrothesaurus.org/uat/1191   |  Solar system gas giant planets   |
|   http://astrothesaurus.org/uat/511    |  Extrasolar rocky planets     |  http://astrothesaurus.org/uat/797    |  Solar system terrestrial planets     |
|   http://astrothesaurus.org/uat/573    |  Galaxies     |  http://astrothesaurus.org/uat/611    |  Galaxy photometry    |
|   http://astrothesaurus.org/uat/573    |  Galaxies     |  http://astrothesaurus.org/uat/2171   |  Galaxy spectroscopy  |
|   http://astrothesaurus.org/uat/611    |  Galaxy photometry    |  http://astrothesaurus.org/uat/573    |  Galaxies     |
|   http://astrothesaurus.org/uat/704    |  Hayashi track    |  http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |
|   http://astrothesaurus.org/uat/721    |  Henyey track     |  http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |
|   http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |  http://astrothesaurus.org/uat/704    |  Hayashi track    |
|   http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |  http://astrothesaurus.org/uat/721    |  Henyey track     |
|   http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |  http://astrothesaurus.org/uat/1842   |  Zero-age horizontal branch stars     |
|   http://astrothesaurus.org/uat/779    |  Impact phenomena     |  http://astrothesaurus.org/uat/958    |  Lunar impacts    |
|   http://astrothesaurus.org/uat/797    |  Solar system terrestrial planets     |  http://astrothesaurus.org/uat/511    |  Extrasolar rocky planets     |
|   http://astrothesaurus.org/uat/958    |  Lunar impacts    |  http://astrothesaurus.org/uat/779    |  Impact phenomena     |
|   http://astrothesaurus.org/uat/974    |  Lunar surface    |  http://astrothesaurus.org/uat/2208   |  Natural satellite surfaces   |
|   http://astrothesaurus.org/uat/999    |  Magnitude    |  http://astrothesaurus.org/uat/1233   |  Photometric systems  |
|   http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |  http://astrothesaurus.org/uat/2212   |  Natural satellite dynamics   |
|   http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |  http://astrothesaurus.org/uat/1425   |  Natural satellite formation  |
|   http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |  http://astrothesaurus.org/uat/2208   |  Natural satellite surfaces   |
|   http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |  http://astrothesaurus.org/uat/2214   |  Natural satellite atmospheres    |
|   http://astrothesaurus.org/uat/1092   |  Near-Earth objects   |  http://astrothesaurus.org/uat/280    |  Comets   |
|   http://astrothesaurus.org/uat/1092   |  Near-Earth objects   |  http://astrothesaurus.org/uat/72     |  Asteroids    |
|   http://astrothesaurus.org/uat/1191   |  Solar system gas giant planets   |  http://astrothesaurus.org/uat/509    |  Extrasolar gaseous giant planets     |
|   http://astrothesaurus.org/uat/1233   |  Photometric systems  |  http://astrothesaurus.org/uat/999    |  Magnitude    |
|   http://astrothesaurus.org/uat/1244   |  Planetary atmospheres    |  http://astrothesaurus.org/uat/116    |  Atmospheric science  |
|   http://astrothesaurus.org/uat/1244   |  Planetary atmospheres    |  http://astrothesaurus.org/uat/2184   |  Planetary climates   |
|   http://astrothesaurus.org/uat/1255   |  Planetary science    |  http://astrothesaurus.org/uat/2191   |  Remote sensing   |
|   http://astrothesaurus.org/uat/1265   |  Plate tectonics  |  http://astrothesaurus.org/uat/493    |  Exoplanet plate tectonics    |
|   http://astrothesaurus.org/uat/1338   |  Radio astronomy  |  http://astrothesaurus.org/uat/1359   |  Radio spectroscopy   |
|   http://astrothesaurus.org/uat/1359   |  Radio spectroscopy   |  http://astrothesaurus.org/uat/1338   |  Radio astronomy  |
|   http://astrothesaurus.org/uat/1368   |  Red giant branch     |  http://astrothesaurus.org/uat/1372   |  Red giant stars  |
|   http://astrothesaurus.org/uat/1372   |  Red giant stars  |  http://astrothesaurus.org/uat/1368   |  Red giant branch     |
|   http://astrothesaurus.org/uat/1425   |  Natural satellite formation  |  http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |
|   http://astrothesaurus.org/uat/1472   |  Solar-planetary interactions     |  http://astrothesaurus.org/uat/2177   |  Star-planet interactions     |
|   http://astrothesaurus.org/uat/1472   |  Solar-planetary interactions     |  http://astrothesaurus.org/uat/2037   |  Space weather    |
|   http://astrothesaurus.org/uat/1528   |  Solar system     |  http://astrothesaurus.org/uat/484    |  Exoplanet systems    |
|   http://astrothesaurus.org/uat/1570   |  Starburst galaxies   |  http://astrothesaurus.org/uat/2176   |  Post-starburst galaxies  |
|   http://astrothesaurus.org/uat/1780   |  Volcanoes    |  http://astrothesaurus.org/uat/2175   |  Tectonics    |
|   http://astrothesaurus.org/uat/1842   |  Zero-age horizontal branch stars     |  http://astrothesaurus.org/uat/725    |  Hertzsprung Russell diagram  |
|   http://astrothesaurus.org/uat/1870   |  Educational software     |  http://astrothesaurus.org/uat/2165   |  Astronomy education  |
|   http://astrothesaurus.org/uat/1964   |  Magnetohydrodynamics     |  http://astrothesaurus.org/uat/23     |  Alfven waves     |
|   http://astrothesaurus.org/uat/2036   |  Main belt asteroids  |  http://astrothesaurus.org/uat/219    |  Ceres    |
|   http://astrothesaurus.org/uat/2036   |  Main belt asteroids  |  http://astrothesaurus.org/uat/70     |  Asteroid belt    |
|   http://astrothesaurus.org/uat/2037   |  Space weather    |  http://astrothesaurus.org/uat/1472   |  Solar-planetary interactions     |
|   http://astrothesaurus.org/uat/2165   |  Astronomy education  |  http://astrothesaurus.org/uat/1870   |  Educational software     |
|   http://astrothesaurus.org/uat/2171   |  Galaxy spectroscopy  |  http://astrothesaurus.org/uat/573    |  Galaxies     |
|   http://astrothesaurus.org/uat/2175   |  Tectonics    |  http://astrothesaurus.org/uat/1780   |  Volcanoes    |
|   http://astrothesaurus.org/uat/2176   |  Post-starburst galaxies  |  http://astrothesaurus.org/uat/1570   |  Starburst galaxies   |
|   http://astrothesaurus.org/uat/2177   |  Star-planet interactions     |  http://astrothesaurus.org/uat/1472   |  Solar-planetary interactions     |
|   http://astrothesaurus.org/uat/2184   |  Planetary climates   |  http://astrothesaurus.org/uat/1244   |  Planetary atmospheres    |
|   http://astrothesaurus.org/uat/2191   |  Remote sensing   |  http://astrothesaurus.org/uat/1255   |  Planetary science    |
|   http://astrothesaurus.org/uat/2203   |  Comet origins    |  http://astrothesaurus.org/uat/280    |  Comets   |
|   http://astrothesaurus.org/uat/2205   |  Exoplanet migration  |  http://astrothesaurus.org/uat/2206   |  Planetary migration  |
|   http://astrothesaurus.org/uat/2206   |  Planetary migration  |  http://astrothesaurus.org/uat/2205   |  Exoplanet migration  |
|   http://astrothesaurus.org/uat/2208   |  Natural satellite surfaces   |  http://astrothesaurus.org/uat/974    |  Lunar surface    |
|   http://astrothesaurus.org/uat/2208   |  Natural satellite surfaces   |  http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |
|   http://astrothesaurus.org/uat/2210   |  Asteroid dynamics    |  http://astrothesaurus.org/uat/72     |  Asteroids    |
|   http://astrothesaurus.org/uat/2212   |  Natural satellite dynamics   |  http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |
|   http://astrothesaurus.org/uat/2213   |  Comet dynamics   |  http://astrothesaurus.org/uat/280    |  Comets   |
|   http://astrothesaurus.org/uat/2214   |  Natural satellite atmospheres    |  http://astrothesaurus.org/uat/1089   |  Natural satellites (Solar system)    |



#### Alternate Labels added to 114 concepts:

| Concept URI | PrefLabel | Alternate Labels |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/0  |  DC stars     |  DC white dwarf stars, DC white dwarf     |
|   http://astrothesaurus.org/uat/8  |  A supergiant stars   |  A-type supergiant stars  |
|   http://astrothesaurus.org/uat/24     |  Algol variable stars     |  Algol-type variables     |
|   http://astrothesaurus.org/uat/31     |  AM Canum Venaticorum stars   |  AM CVn stars     |
|   http://astrothesaurus.org/uat/46     |  Antapex  |  Solar antapex    |
|   http://astrothesaurus.org/uat/52     |  Interstellar objects     |  Aperiodic comets, Interstellar comets    |
|   http://astrothesaurus.org/uat/54     |  Apex     |  Solar apex   |
|   http://astrothesaurus.org/uat/72     |  Asteroids    |  Minor planets, Asteroid  |
|   http://astrothesaurus.org/uat/95     |  Astronomical unit    |  au, AU   |
|   http://astrothesaurus.org/uat/138    |  Baryon acoustic oscillations     |  BAO  |
|   http://astrothesaurus.org/uat/174    |  Bondi accretion  |  Bondi-Hoyle accretion    |
|   http://astrothesaurus.org/uat/215    |  Centaur group    |  Centaur asteroids, Centaurs  |
|   http://astrothesaurus.org/uat/216    |  Center of mass   |  Center of gravity    |
|   http://astrothesaurus.org/uat/219    |  Ceres    |  Asteroid Ceres, (1) Ceres, 1 Ceres   |
|   http://astrothesaurus.org/uat/258    |  Earth's clouds   |  Clouds   |
|   http://astrothesaurus.org/uat/270    |  Coma Cluster     |  Abell 1656   |
|   http://astrothesaurus.org/uat/348    |  DA stars     |  DA white dwarf, DA white dwarf stars     |
|   http://astrothesaurus.org/uat/358    |  DB stars     |  DB white dwarf, DB white dwarf stars     |
|   http://astrothesaurus.org/uat/360    |  DDO photometry   |  DDO photometric system   |
|   http://astrothesaurus.org/uat/388    |  Dirty snowball model     |  Dirty iceball model  |
|   http://astrothesaurus.org/uat/396    |  Diurnal parallax     |  Geocentric parallax  |
|   http://astrothesaurus.org/uat/397    |  DO stars     |  DO white dwarf stars, DO white dwarf     |
|   http://astrothesaurus.org/uat/415    |  Dwarf elliptical galaxies    |  dE, dEs  |
|   http://astrothesaurus.org/uat/445    |  Ecliptic coordinate system   |  Ecliptic system  |
|   http://astrothesaurus.org/uat/452    |  Einstein universe    |  Einstein static Universe     |
|   http://astrothesaurus.org/uat/509    |  Extrasolar gaseous giant planets     |  Extrasolar gas giants    |
|   http://astrothesaurus.org/uat/642    |  Geneva photometry    |  Geneva photometric system    |
|   http://astrothesaurus.org/uat/653    |  Giant molecular clouds   |  GMC  |
|   http://astrothesaurus.org/uat/715    |  Helium-rich stars    |  Helium strong stars  |
|   http://astrothesaurus.org/uat/717    |  Helium-weak stars    |  Helium poor stars, Helium weak stars, Helium-poor stars  |
|   http://astrothesaurus.org/uat/719    |  Henry Draper catalog     |  Henry Draper Catalogue   |
|   http://astrothesaurus.org/uat/733    |  High mass x-ray binary stars     |  HMXB     |
|   http://astrothesaurus.org/uat/741    |  Hilda group  |  Hilda asteroids  |
|   http://astrothesaurus.org/uat/758    |  Hubble constant  |  Hubble-Lemaitre constant     |
|   http://astrothesaurus.org/uat/763    |  Hubble-Lemaitre law  |  Hubble's law     |
|   http://astrothesaurus.org/uat/787    |  Infrared dark clouds     |  IRDC     |
|   http://astrothesaurus.org/uat/797    |  Solar system terrestrial planets     |  Terrestrial planets, Inner planets   |
|   http://astrothesaurus.org/uat/837    |  Interstellar dust extinction     |  Interstellar extinction  |
|   http://astrothesaurus.org/uat/860    |  Earth ionosphere     |  Earth's ionosphere   |
|   http://astrothesaurus.org/uat/872    |  Jovian satellites    |  Jupiter's moons, Jupiter's satellites    |
|   http://astrothesaurus.org/uat/882    |  Kappa mechanism  |  κ-mechanism  |
|   http://astrothesaurus.org/uat/889    |  Kirkwood gaps    |  Kirkwood gap     |
|   http://astrothesaurus.org/uat/890    |  Kreutz group     |  Kreutz sungrazers    |
|   http://astrothesaurus.org/uat/903    |  Large Magellanic Cloud   |  LMC  |
|   http://astrothesaurus.org/uat/940    |  Low surface brightness galaxies  |  UDG, Ultradiffuse galaxies, Ultra-diffuse galaxy, Ultra diffuse galaxy, Ultra-diffuse galaxies, Ultra diffuse galaxies, Ultradiffuse galaxy  |
|   http://astrothesaurus.org/uat/944    |  Luminous blue variable stars     |  LBV  |
|   http://astrothesaurus.org/uat/946    |  Luminous infrared galaxies   |  IRAS galaxies    |
|   http://astrothesaurus.org/uat/976    |  Lunar transient phenomena    |  TLP, Transient lunar phenomenon  |
|   http://astrothesaurus.org/uat/997    |  Planetary magnetospheres     |  Planetary magnetosphere  |
|   http://astrothesaurus.org/uat/1035   |  Meteor streams   |  Meteoroid stream     |
|   http://astrothesaurus.org/uat/1039   |  Meteoroid dust clouds    |  Meteoroid dust   |
|   http://astrothesaurus.org/uat/1092   |  Near-Earth objects   |  Near Earth objects   |
|   http://astrothesaurus.org/uat/1169   |  Optical observation  |  Visual observation   |
|   http://astrothesaurus.org/uat/1187   |  Orreries     |  Orrery   |
|   http://astrothesaurus.org/uat/1191   |  Solar system gas giant planets   |  Jovian planets, Gas giants, Outer planets    |
|   http://astrothesaurus.org/uat/1233   |  Photometric systems  |  Magnitude systems    |
|   http://astrothesaurus.org/uat/1267   |  Pluto    |  134340 Pluto, (134340) Pluto     |
|   http://astrothesaurus.org/uat/1292   |  Primordial black holes   |  Mini black hole  |
|   http://astrothesaurus.org/uat/1301   |  Protoplanetary nebulae   |  PPN  |
|   http://astrothesaurus.org/uat/1307   |  Pulsating variable stars     |  Pulsating stars  |
|   http://astrothesaurus.org/uat/1356   |  Radio source catalogs    |  Cambridge Catalogue of Radio Sources     |
|   http://astrothesaurus.org/uat/1403   |  Ritchey-Chrétien telescopes  |  Ritchey-Chretien telescopes  |
|   http://astrothesaurus.org/uat/1423   |  Sagittarius dwarf spheroidal galaxy  |  Sgr dE, Sag DEG, Sgr dSph    |
|   http://astrothesaurus.org/uat/1425   |  Natural satellite formation  |  Satellite formation  |
|   http://astrothesaurus.org/uat/1428   |  Scalar-tensor-vector gravity     |  Modified gravity     |
|   http://astrothesaurus.org/uat/1452   |  Short period comets  |  Short-period comet   |
|   http://astrothesaurus.org/uat/1453   |  Short period variable stars  |  Short-period variable stars, Short-period variables, Short-period variable, Short period variable, Short period variables    |
|   http://astrothesaurus.org/uat/1468   |  Small Magellanic Cloud   |  SMC  |
|   http://astrothesaurus.org/uat/1469   |  Small Solar System bodies    |  Minor planets, Small Solar System body   |
|   http://astrothesaurus.org/uat/1473   |  Solar-terrestrial interactions   |  Solar terrestrial relation, Sun-Earth interactions   |
|   http://astrothesaurus.org/uat/1565   |  Star forming regions     |  Star formation regions   |
|   http://astrothesaurus.org/uat/1570   |  Starburst galaxies   |  Starburst galaxy     |
|   http://astrothesaurus.org/uat/1641   |  Strömgren photometry     |  Strömgren photometric system, uvbyβ photometric system, Stromgren photometry     |
|   http://astrothesaurus.org/uat/1682   |  Tailed radio galaxies    |  Head-tail galaxies   |
|   http://astrothesaurus.org/uat/1708   |  Transit instruments  |  Transit telescopes   |
|   http://astrothesaurus.org/uat/1758   |  Van Allen radiation belts    |  Van Allen belts  |
|   http://astrothesaurus.org/uat/1771   |  Vilnius photometry   |  Vilnius photometric system   |
|   http://astrothesaurus.org/uat/1776   |  Optical astronomy    |  Visible astronomy    |
|   http://astrothesaurus.org/uat/1780   |  Volcanoes    |  Volcano  |
|   http://astrothesaurus.org/uat/1785   |  Walraven photometry  |  Walraven photometric system  |
|   http://astrothesaurus.org/uat/1834   |  Young stellar objects    |  YSOs     |
|   http://astrothesaurus.org/uat/1839   |  Zenith hourly rate   |  Zenith hour rate     |
|   http://astrothesaurus.org/uat/1848   |  DZ stars     |  DZ white dwarf stars, DZ white dwarf     |
|   http://astrothesaurus.org/uat/1849   |  DQ stars     |  DQ white dwarf stars, DQ white dwarf     |
|   http://astrothesaurus.org/uat/1852   |  X-ray transient sources  |  X-ray transient  |
|   http://astrothesaurus.org/uat/1853   |  Gamma-ray transient sources  |  Gamma ray transient source, γ-ray transient source, γ-ray transient sources  |
|   http://astrothesaurus.org/uat/1941   |  Solar analogs    |  Solar-like star  |
|   http://astrothesaurus.org/uat/2039   |  Solar coronal plumes     |  Polar plume, Solar polar plume   |
|   http://astrothesaurus.org/uat/2044   |  Morgan-Keenan classification     |  Yerkes spectral classification, Morgan-Keenan-Kellman classification, MKK classification, Yerkes classification  |
|   http://astrothesaurus.org/uat/2045   |  Schonberg-Chandrasekhar limit    |  Schönberg-Chandrasekhar limit    |
|   http://astrothesaurus.org/uat/2050   |  Low mass stars   |  Low-mass star    |
|   http://astrothesaurus.org/uat/2079   |  Pre-biotic astrochemistry    |  Prebiotic astrochemistry, Prebiotic chemistry, Pre-biotic chemistry  |
|   http://astrothesaurus.org/uat/2127   |  Search for extraterrestrial intelligence     |  SETI     |
|   http://astrothesaurus.org/uat/2163   |  Flat-spectrum radio quasars  |  Core-dominated quasar, FSRQ, HPQ, OVV quasar, Highly polarized quasar, Optically violent variable quasar, CDQ, Highly polarized quasars, Core-dominated quasars, Optically violent variable quasars, OVV quasars     |
|   http://astrothesaurus.org/uat/2164   |  Ultraluminous x-ray sources  |  ULS, Luminous supersoft x-ray source, Pulsating ultraluminous X-ray sources, PULX, Ultraluminous supersoft sources, SSS, Supersoft sources, ULX,  SSXS   |
|   http://astrothesaurus.org/uat/2168   |  AB photometry    |  AB magnitude, AB magnitude system, AB photometric system     |
|   http://astrothesaurus.org/uat/2169   |  Vega photometry  |  Vega photometric system  |
|   http://astrothesaurus.org/uat/2170   |  Extreme ultraviolet astronomy    |  EUV astronomy, EUV   |
|   http://astrothesaurus.org/uat/2172   |  Extrasolar gaseous planets   |  Extrasolar gas planets   |
|   http://astrothesaurus.org/uat/2176   |  Post-starburst galaxies  |  Post starburst galaxy, Post-starburst galaxy, Post starburst galaxies, PSB   |
|   http://astrothesaurus.org/uat/2177   |  Star-planet interactions     |  Stellar-planetary interactions, Star-exoplanet interactions  |
|   http://astrothesaurus.org/uat/2181   |  Comet Halley     |  Halley's comet, 1P/Halley    |
|   http://astrothesaurus.org/uat/2182   |  Eros     |  (433) Eros, 433 Eros, Asteroid Eros  |
|   http://astrothesaurus.org/uat/2183   |  Vesta    |  4 Vesta, Asteroid Vesta, (4) Vesta   |
|   http://astrothesaurus.org/uat/2188   |  Ganymede     |  Jupiter III  |
|   http://astrothesaurus.org/uat/2189   |  Europa   |  Jupiter II   |
|   http://astrothesaurus.org/uat/2190   |  Io   |  Jupiter I    |
|   http://astrothesaurus.org/uat/2194   |  Zodiacal dust bands  |  Dust bands, IRAS dust bands  |
|   http://astrothesaurus.org/uat/2196   |  Sundivers    |  Sun-plunging comet, Sun-plunging, Sun-plunging comets, Sun-plunger   |
|   http://astrothesaurus.org/uat/2199   |  Kracht group     |  Kracht sunskirters   |
|   http://astrothesaurus.org/uat/2200   |  Meyer group  |  Meyer sunskirters    |
|   http://astrothesaurus.org/uat/2201   |  Marsden group    |  Marsden sunskirters  |
|   http://astrothesaurus.org/uat/2202   |  Plutonian satellites     |  Moons of Pluto, Charon, Pluto's moons    |
|   http://astrothesaurus.org/uat/2207   |  Asteroid satellites  |  Multi-body asteroids, Multiple SSSB systems, Double asteroids, Minor planet moons, Asteroid moons, Multiple small Solar System bodies, Binary SSSBs, Binary small Solar System body systems, Multiple systems, Satellites of asteroids, Multiple SSSBs, Multiple asteroids, Binary asteroids, Binary small Solar System bodies, Binary systems, Binary SSSB systems, Asteroid multiples, Multiple small Solar System body systems    |


#### Definitions added to 854 concepts:
[See full list of new definitions](release_notes_definitions_UAT_4.0.0.md)


#### Scope Notes added to 9 concepts:

| Concept URI | PrefLabel | Scope Note |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/148    |  Beta Cephei variable stars   |  These stars are usually hot blue-white stars of spectral class B and should not be confused with Cepheid variables, which are named after Delta Cephei and are luminous supergiant stars. -- Wikipedia, https://en.wikipedia.org/wiki/Beta_Cephei_variable   |
|   http://astrothesaurus.org/uat/215    |  Centaur group    |  Not to be confused with Centaurus meteor shower.     |
|   http://astrothesaurus.org/uat/678    |  Gravitational waves  |  Not to be confused with a gravity wave.  |
|   http://astrothesaurus.org/uat/848    |  Interstellar medium wind     |  Wind that a star perceives from the ISM.     |
|   http://astrothesaurus.org/uat/1169   |  Optical observation  |  Astronomy using the (human) eye as the primary detector; this includes both naked-eye observations and observations through telescopes without further instrumentation (like cameras, spectrographs, etc).   |
|   http://astrothesaurus.org/uat/1472   |  Solar-planetary interactions     |  Specific to interactions between the Sun and Solar system planets.  The similar concept "Star-planet interactions" is about exoplanets and their stars.  |
|   http://astrothesaurus.org/uat/1473   |  Solar-terrestrial interactions   |  Specific to interactions between the Sun and Earth.  The similar concept "Solar-planetary interactions" is about interactions between the Sun and other Solar system planets, or all of them more generally.     |
|   http://astrothesaurus.org/uat/2110   |  Blazhko effect   |  This is phenomenon observed in RR Lyr type stars and demonstrates as changes of the light curve on timescales longer than pulsation period. The effect was first found more than 100 years ago and its origin is still not well understood and subject of active research. - https://github.com/astrothesaurus/UAT/issues/286    |
|   http://astrothesaurus.org/uat/2111   |  Double periodic variable stars   |  Some of the binary stars show additional period that this ~33 times longer than the orbital period and this group is called DPVs. Most of these systems are also showing eclipses, but that's not required. DPVs studied in detail show circumprimary discs. Note that the name seems general, but refers to only a specific group of binary stars. -- https://github.com/astrothesaurus/UAT/issues/286  |
|   http://astrothesaurus.org/uat/2112   |  Blue large-amplitude pulsators   |  A class of pulsating variable stars with short periods. These stars are hot (hence "blue" in name) and show relatively large amplitudes. The evolutionary state of these stars is not known. -- https://github.com/astrothesaurus/UAT/issues/286     |
|   http://astrothesaurus.org/uat/2135   |  Stellar occultation  |  Occultation of a star by another object.     |
|   http://astrothesaurus.org/uat/2165   |  Astronomy education  |  Refers to both methods currently used to teach the science of astronomy and to an area of pedagogical research that seeks to improve those methods.  |
|   http://astrothesaurus.org/uat/2177   |  Star-planet interactions     |  Interactions between exoplanets and their stars.  The similar concept "Solar-planetary interactions" is specific to interactions between the Sun and Solar system planets.   |
|   http://astrothesaurus.org/uat/2191   |  Remote sensing   |  Intended to cover planetary remote sensing, a "catch-all term for any planetary work using remote observations. It would include radar, but also VNIR, TIR, etc. wavelengths."   |


#### Examples added to 14 concepts:

| Concept URI | PrefLabel | Scope Note |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/52     |  Interstellar objects     |  2I/Borisov, 1I/'Oumuamua     |
|   http://astrothesaurus.org/uat/280    |  Comets   |  P/Shoemaker-Levy 9, 109P/Swift-Tuttle    |
|   http://astrothesaurus.org/uat/419    |  Dwarf planets    |  Eris, Makemake   |
|   http://astrothesaurus.org/uat/872    |  Jovian satellites    |  Leda, Thebe, Amalthea    |
|   http://astrothesaurus.org/uat/1009   |  Martian satellites   |  Phobos, Deimos   |
|   http://astrothesaurus.org/uat/1098   |  Neptunian satellites     |  Naiad, Nereid, Thalassa  |
|   http://astrothesaurus.org/uat/1427   |  Saturnian satellites     |  Dione, Mimas, Tethys, Enceladus  |
|   http://astrothesaurus.org/uat/1750   |  Uranian satellites   |  Ariel, Umbriel, Oberon, Titania  |
|   http://astrothesaurus.org/uat/2202   |  Plutonian satellites     |  Charon, Styx, Hydra, Kerberos, Nix   |


#### Deprecated 27 Concepts:

| Deprecated Concept URI | Deprecated Concept PrefLabel | Reason |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/175    |  Borasisi     | Low usage in literature |
|   http://astrothesaurus.org/uat/222    |  Chaos    | Low usage in literature, also mistaken for "unpredictability" |
|   http://astrothesaurus.org/uat/243    |  Cirrus castellanus   | Low usage in literature |
|   http://astrothesaurus.org/uat/244    |  Cirrus fibratus  | Low usage in literature |
|   http://astrothesaurus.org/uat/245    |  Cirrus floccus   | Low usage in literature |
|   http://astrothesaurus.org/uat/246    |  Cirrus spissatus     | Low usage in literature |
|   http://astrothesaurus.org/uat/247    |  Cirrus uncinus   | Low usage in literature |
|   http://astrothesaurus.org/uat/248    |  Cirrus vertebratus   | Low usage in literature |
|   http://astrothesaurus.org/uat/377    |  Deucalion    | Low usage in literature |
|   http://astrothesaurus.org/uat/473    |  Eris     | Low usage in literature |
|   http://astrothesaurus.org/uat/702    |  Haumea   | Low usage in literature |
|   http://astrothesaurus.org/uat/714    |  Helium-poor stars    | Duplicate concept, merged into Helium-weak stars (http://astrothesaurus.org/uat/717) |
|   http://astrothesaurus.org/uat/766    |  Huya     | Low usage in literature |
|   http://astrothesaurus.org/uat/862    |  IRAS galaxies    | Duplicate concept, merged into Luminous infrared galaxies (http://astrothesaurus.org/uat/946) |
|   http://astrothesaurus.org/uat/868    |  Ixion    | Low usage in literature |
|   http://astrothesaurus.org/uat/930    |  Logos    | Low usage in literature |
|   http://astrothesaurus.org/uat/1002   |  Makemake     | Low usage in literature |
|   http://astrothesaurus.org/uat/1065   |  Minor planets    | Duplicate concept, merged into Small Solar System bodies (http://astrothesaurus.org/uat/1469) |
|   http://astrothesaurus.org/uat/1115   |  Noctilucent clouds   | Low usage in literature |
|   http://astrothesaurus.org/uat/1185   |  Orcus    | Low usage in literature |
|   http://astrothesaurus.org/uat/1315   |  Quaoar   | Low usage in literature |
|   http://astrothesaurus.org/uat/1440   |  Sedna    | Low usage in literature |
|   http://astrothesaurus.org/uat/1575   |  Stefan's quintet     | Low usage in literature |
|   http://astrothesaurus.org/uat/1685   |  Teharonhiawako   | Low usage in literature |
|   http://astrothesaurus.org/uat/1762   |  Varuna   | Low usage in literature |
|   http://astrothesaurus.org/uat/1778   |  Visual observation   | Duplicate concept, merged into Optical observation (http://astrothesaurus.org/uat/1169) |
|   http://astrothesaurus.org/uat/1830   |  Yerkes classification    | Duplicate concept, merged into Morgan-Keenan classification (http://astrothesaurus.org/uat/2044) |


#### Removed 2 related concept links:

| Concept URI | Concept PrefLabel | Related Concept URI | Related Concept PrefLabel |
| --- | --- | --- | --- |
|   http://astrothesaurus.org/uat/70     |  Asteroid belt    |  http://astrothesaurus.org/uat/219    |  Ceres    |
|   http://astrothesaurus.org/uat/219    |  Ceres    |  http://astrothesaurus.org/uat/70     |  Asteroid belt    |


#### Removed alternate labels from 15 concepts:

| Concept URI | PrefLabel | Removed AltLabels |
| --- | --- | --- |
|   http://astrothesaurus.org/uat/8  |  A supergiant stars   |  A-type sueprgiant stars  |
|   http://astrothesaurus.org/uat/509    |  Extrasolar gaseous giant planets     |  Giant planets, Jovian planets    |
|   http://astrothesaurus.org/uat/627    |  Galilean satellites  |  Ganymede, Europa, Io     |
|   http://astrothesaurus.org/uat/882    |  Kappa mechanism  |  κ–mechanism  |
|   http://astrothesaurus.org/uat/890    |  Kreutz group     |  Sungrazer    |
|   http://astrothesaurus.org/uat/1039   |  Meteoroid dust clouds    |  Meteroid dust    |
|   http://astrothesaurus.org/uat/1098   |  Neptunian satellites     |  Triton   |
|   http://astrothesaurus.org/uat/1356   |  Radio source catalogs    |  Cambridgte Catalogue of Radio Sources    |
|   http://astrothesaurus.org/uat/1403   |  Ritchey-Chrétien telescopes  |  Ritchey–Chretien telescopes  |
|   http://astrothesaurus.org/uat/1427   |  Saturnian satellites     |  Titan    |
|   http://astrothesaurus.org/uat/1428   |  Scalar-tensor-vector gravity     |  MOdified Gravity     |
|   http://astrothesaurus.org/uat/1473   |  Solar-terrestrial interactions   |  Solar terrestiral relation   |
|   http://astrothesaurus.org/uat/1641   |  Strömgren photometry     |  Strömgren photometry     |
|   http://astrothesaurus.org/uat/1834   |  Young stellar objects    |  YSOS     |
|   http://astrothesaurus.org/uat/1853   |  Gamma-ray transient sources  |  γ-ray transiet source, γ-ray transiet sources, Gamma ray transiet source     |