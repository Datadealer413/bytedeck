# Generated by Django 2.2.12 on 2020-05-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djcytoscape', '0005_auto_20200403_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cytostyleset',
            name='init_options',
            field=models.TextField(blank=True, default='minZoom: 0.5, \nmaxZoom: 1.5, \nwheelSensitivity: 0.1, \nzoomingEnabled: false, \nuserZoomingEnabled: false, \nautoungrabify: true,\nautounselectify: true,\n', help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#core/initialisation)', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='javascript',
            field=models.TextField(blank=True, default="// cursors\n  // links\n    cy.on('mouseover', '[href]', function(){\n        $('#cy').css('cursor', 'pointer');\n        this.addClass('link_hover')\n    });\n\n    cy.on('mouseout', '[href]', function(){\n        $('#cy').css('cursor', 'move');\n        this.removeClass('link_hover')\n    });\n  // none link nodes\n    cy.on('mouseover', '[^href]', function(){\n        $('#cy').css('cursor', 'default');\n    });\n     cy.on('mouseout', '[^href]', function(){\n        $('#cy').css('cursor', 'move');\n    });\n\n\n$(document).ready(function() { \n  updateBounds();\n  cy.on('ready', function () {\n    updateBounds();\n  });\n  //if they resize the window, resize the diagram\n  $(window).resize(function () {\n    updateBounds();\n  });\n    cy.center();\n    cy.resize();\n\n\n}); // dom ready\n\nvar updateBounds = function () {\n    var bounds = cy.elements().boundingBox();\n    $('#cy').css('height', bounds.h + 50);\n    cy.center();\n    cy.resize();\n};\n", help_text='Will be placed inside script tags. JQuery available. See http://js.cytoscape.org/#core', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='node_styles',
            field=models.TextField(blank=True, default="'label':         'data(label)', \n'text-valign':   'center', 'text-halign': 'right', \n'text-margin-x': '-155', \n'text-wrap': 'wrap',\n'text-max-width': 150,\n'background-position-x': 0,\n'height': 24,\n'font-size': 12,\n'background-fit':'contain', \n'shape':         'roundrectangle', \n'background-opacity': 0, \n'background-position-x': 0, \n'width':         180, \n'border-width':  1, \n'padding-right': 5, 'padding-left':5, 'padding-top':5, 'padding-bottom':5, \n'text-events':   'yes',", help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#style)', null=True),
        ),
    ]