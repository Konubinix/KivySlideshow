#!/bin/bash

buildozer android debug deploy
adb install -r "bin/$(ls bin|tail -1)"
