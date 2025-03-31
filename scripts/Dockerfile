# ***************************************************************** #
# (C) Copyright IBM Corporation 2024.                               #
#                                                                   #
# The source code for this program is not published or otherwise    #
# divested of its trade secrets, irrespective of what has been      #
# deposited with the U.S. Copyright Office.                         #
# ***************************************************************** #
# SPDX-License-Identifier: Apache-2.0
FROM registry.access.redhat.com/ubi9/python-311 as base

WORKDIR /opt

FROM base as local

COPY dist/kubernetes_lite*.whl ./

RUN pip3 install *.whl

FROM base as remote

RUN pip3 install kubernetes_lite


FROM ${build_layer} as examples

COPY examples examples
