def test_tmpdir(tmpdir):
    """
    Demonstrate the built-in pytest tmpdir fixture.
    
    tmpdir provides a temporary directory unique to the test function.
    """
    # tmpdir already has a path associated with it
    # join() extends the path to include a filename (does not create file yet)
    a_file = tmpdir.join('something.txt')

    # You can create subdirectories
    a_sub_dir = tmpdir.mkdir('anything')

    # You can create files in subdirectories (created when written)
    another_file = a_sub_dir.join('something_else.txt')

    # Writing to the file creates it
    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    # Reading the files
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    """
    Demonstrate the pytest tmpdir_factory fixture.

    tmpdir_factory allows creating multiple temporary directories across tests.
    """
    # Create a new temporary directory named 'mydir'
    a_dir = tmpdir_factory.mktemp('mydir')

    # Optionally, get the base temporary directory for all tmpdir_factory dirs
    base_temp = tmpdir_factory.getbasetemp()
    print('base temporary directory:', base_temp)

    # Create a file in the temporary directory
    a_file = a_dir.join('something.txt')

    # Create a subdirectory
    a_sub_dir = a_dir.mkdir('anything')

    # Create a file inside the subdirectory
    another_file = a_sub_dir.join('something_else.txt')

    # Write to the files (creates them)
    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    # Read and verify the file contents
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
