# ***************************************************************** #
# (C) Copyright IBM Corporation 2024.                               #
#                                                                   #
# The source code for this program is not published or otherwise    #
# divested of its trade secrets, irrespective of what has been      #
# deposited with the U.S. Copyright Office.                         #
# ***************************************************************** #
# SPDX-License-Identifier: Apache-2.0

ARG BUILD_LAYER=local

FROM registry.access.redhat.com/ubi9/python-311 as base

USER default

FROM base as build

WORKDIR /opt/build

COPY --chown=default:default scripts/install_build_reqs.py install_build_reqs.py

RUN eval $(python3 install_build_reqs.py)

COPY  --chown=default:default README.md README.md
COPY  --chown=default:default LICENSE LICENSE
COPY  --chown=default:default pyproject.toml pyproject.toml
COPY  --chown=default:default kubernetes_lite kubernetes_lite

RUN pip3 install build && python3 -m build && pip3 install dist/*.whl


FROM build as test

COPY tests tests
RUN pip3 install -e ".[test]"

FROM base as release

COPY --from=build /opt/build/dist/*.whl /opt/dist/

RUN pip3 install /opt/dist/*