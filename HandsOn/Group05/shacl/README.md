---
author: Dim Hoogeveen
title: README
---

# Remarks on SHACL-files

`Report-updated.ttl` shows that there are `8584` violations, these are because of the following:

- RMLmapper generates empty literals (`""`) which are a violation of the `xsd:double` data type. Almost all of these violations are from these.
- One violation is that there is a `R` instead of an integer value in the `pproc:informationKind` of subject `http://eit-upm-opendata.com/ted/CAE/20188511SE`. 