import requests
import codecs
from flask import Flask, render_template, request
from cmislib import CmisClient, Repository