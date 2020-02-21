# Lint as: python3
# Copyright 2019 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Install script for setuptools."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='rlax',
    url='https://github.com/deepmind/haiku',
    license='Apache 2.0',
    author='DeepMind',
    description=('A library of reinforcement learning building blocks in JAX.'),
    author_email='rlax-dev@google.com',
    keywords='reinforcement-learning python machine learning',
    packages=find_packages(),
    install_requires=[
        'absl-py>=0.7.1',
        'jax>=0.1.55',
        'jaxlib>=0.1.37',
        'dm-env>=1.2',
        'numpy>=1.18.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
