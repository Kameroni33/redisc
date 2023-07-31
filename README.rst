=================================================
Credis
=================================================

A minimal, optimized Redis client written in Cython intended for real-time, linux-based applications. This is a fork from the original PyPI package `credis <https://pypi.org/project/credis/>`_.

Example Usages
-------------------------------------------------

The ``credis.Connection.execute`` commands allows a python client to execute a single Redis command.

.. code-block::

    from src.credis import Connection

    # create a connection with redis-server on localhost:6379
    connection = Connection(host='127.0.0.1', port=6379)

    # set a value in redis
    response = connection.execute('SET', 'test', 1)
    print(response)

    # get a value from redis
    response = connection.execute('GET', 'test')
    print(response)

.. code-block::

    'OK'
    1

The ``credis.Connection.execute_pipeline`` commands allows a python client to execute a series of pipelined Redis commands over a single network connection.

.. code-block::

    from src.credis import Connection

    # create a connection with redis-server on localhost:6379
    connection = Connection(host='127.0.0.1', port=6379)

    # send a series of command to Redis in a pipeline
    pipeline = [('SET', f'test{i}', i) for i in range(3)]
    response = connection.execute_pipeline(*pipeline)
    print(response)

.. code-block::

    ('OK', 'OK', 'OK')

The ``credis.ResourcePool`` class allows a python client to set up a pool of network connections with a Redis server. Then, when executing Redis commands the python client will pick the next available connection to send its request over.

.. code-block::

    from src.credis import ResourcePool

    # create a pool of connections with a redis-server on localhost:6379
    pool = ResourcePool(32, Connection, host='127.0.0.1', port=6379)

    # execute a redis command using `with`
    with pool.ctx() as connection:
        response = connection.execute('SET', 'test', 1)
        print(response)

    # execute a redis command directly
    response = pool.execute('GET', 'test')
    print(response)

    # execute a pipeline of commands
    pipeline = [('SET', f'test{i}', i) for i in range(3)]
    response = connection.execute_pipeline(*pipeline)
    print(response)

.. code-block::

    'OK'
    1
    ('OK', 'OK', 'OK')


For a full list of Redis commands, see the [Redis Documentation](https://redis.io/commands/).

Development
-------------------------------------------------

You can clone the repository to your local machine from `GitHub <https://github.com/Kameroni33/redisc>`_ or using the following command:

.. code-block::

    git clone https://github.com/Kameroni33/redisc

Depending on your needs, you can download the requirements to build/deploy the project to PyPI, run tests, or benchmark the system. Note that in all cases you will need the general requirements.

.. code-block::

    python3 -m pip install .             # general requirements
    python3 -m pip install .[deploy]     # deployment requirements
    python3 -m pip install .[test]       # unit test requirements
    python3 -m pip install .[benchmark]  # benchmarking requirements

The following commands let you build both the source distribution and platform specific distributions. Note that eggs are now outdated and PyPI will no longer accept them with version 23.3.

.. code-block::

    python3 setup.py sdist        # build source distribution
    python3 setup.py bdist        # build platform specific distribution
    python3 setup.py bdist_egg    # build package egg (outdated)
    python3 setup.py bdist_wheel  # build package wheel

When uploading distribution files to PyPI, you need an authentication token. Please reach out to the repo author regarding PyPI permissions.

.. code-block::

    python3 -m twine upload --repository testpypi dist/*  # upload to 'test' server
