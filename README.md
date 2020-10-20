[![Build Status](https://travis-ci.org/submarcos/django-vectortiles.svg?branch=master)](https://travis-ci.org/submarcos/django-vectortiles/)
[![codecov](https://codecov.io/gh/submarcos/django-vectortiles/branch/master/graph/badge.svg)](https://codecov.io/gh/submarcos/django-vectortiles)

![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)
![Django Version](https://img.shields.io/badge/django-%3E%3D%202.2-blue.svg)

# Generate MapBox VectorTiles from GeoDjango models

## With mapbox_vector_tile or directly with PostgreSQL/PostGIS 2.4+


### Installation

#### Basic
```bash
pip install django-vectortiles
```

* Without any other option, use only vectortiles.postgis
* Ensure you have psycopg2 set and installed

#### If you don't want to use Postgis
```bash
pip install django-vectortiles[mapbox]
```
* This will incude mapbox_vector_tiles package and its dependencies
* Use only vectortiles.mapbox

### Simple model example:

```python
# in your view file

from django.views.generic import ListView
from vectortiles.postgis.views import PostgisVectorTileView
from yourapp.models import Feature


class FeatureTileView(PostgisVectorTileView, ListView):
    model = Feature
    vector_tile_layer_name = "features"
    vector_tile_fields = ('other_field_to_include', )


# in your urls file
from django.urls import path
from yourapp import views


urlpatterns = [
    ...
    path('tiles/<int:z>/<int:x>/<int:y>', views.PostGISFeatureView.as_view(), name="feature-tile"),
    ...
]
```

### Related model example:

```python
# in your view file

from django.views.generic import DetailView
from vectortiles.mixins import BaseVectorTileView
from vectortiles.postgis.views import PostgisVectorTileView
from yourapp.models import Layer


class LayerTileView(PostgisVectorTileView, DetailView):
    model = Layer
    vector_tile_fields = ('other_field_to_include', )

    def get_vector_tile_layer_name(self):
        return self.get_object().name

    def get_vector_tile_queryset(self):
        return self.get_object().features.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return BaseVectorTileView.get(self,request=request, z=kwargs.get('z'), x=kwargs.get('x'), y=kwargs.get('y'))


# in your urls file
from django.urls import path
from yourapp import views


urlpatterns = [
    ...
    path('layer/<int:pk>/tile/<int:z>/<int:x>/<int:y>', views.LayerTileView.as_view(), name="layer-tile"),
    ...
]
```

### Usage without PostgreSQL / PostGIS

Just import and use vectortiles.mapbox.view.MapboxVectorTileVew instead of vectortiles.postgis.view.PostgisVectorTileView

### Usage with DRF

django-vectortiles can be used with DRF, use right BaseMixin and action on viewsets, or directly a GET method in an APIView.

-> vectortiles.mapbox.mixins.MapboxBaseVectorTile and vectortiles.postgis.mixins.PostgisBaseVectorTile

### Development

#### With docker and docker-compose

```bash
docker pull makinacorpus/geodjango:bionic-3.6
docker-compose build
# docker-compose up
docker-compose run /code/venv/bin/python ./manage.py test
```

### Local

* Install python and django requirements (python 3.6+, django 2.2+)
* Install geodjango requirements
* Have a postgresql / postgis 2.4+ enabled database
* Use a virtualenv
```bash
pip install .[dev] -U
```
