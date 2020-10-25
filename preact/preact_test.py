import os
from os import replace
from preact import Manager
import shutil

MANAGER = Manager()


def test_module() -> None:
    try:
        MANAGER.setName("moduleTest")
        MANAGER.createModule()
        compareFiles("index.tsx", "moduleTest")
        compareFiles("style.css", "moduleTest", False)
        compareFiles("style.css.d.ts", "moduleTest", False)
        print("[Test Module] - Success - created, compared, deleted")
    finally:
        shutil.rmtree(os.path.join(
            os.path.abspath(os.getcwd()), "moduleTest"), ignore_errors=True)


def test_file() -> None:
    try:
        MANAGER.setName("fileTest")
        MANAGER.createFile()
        compareFiles("index.tsx", "fileTest")
        print("[Test File] - Success - created, compared, deleted")
    finally:
        shutil.rmtree(os.path.join(
            os.path.abspath(os.getcwd()), "fileTest"), ignore_errors=True)


def test_module_with_storybook() -> None:
    try:
        MANAGER.setName("moduleTestStory")
        MANAGER.createModule()
        MANAGER.createStorybook()
        compareFiles("index.tsx", "moduleTestStory")
        compareFiles("style.css", "moduleTestStory", False)
        compareFiles("style.css.d.ts", "moduleTestStory", False)
        compareFiles("index.stories.tsx", "moduleTestStory")
        print("[Test Module Storybook] - Success - created, compared, deleted")
    finally:
        shutil.rmtree(os.path.join(
            os.path.abspath(os.getcwd()), "moduleTestStory"), ignore_errors=True)


def compareFiles(filename: str, module: str = "", replace: bool = True) -> None:
    wdir = os.path.abspath(os.getcwd())
    testFile = open(os.path.join(wdir, "{m}/{n}".format(m=module, n=filename)))
    solutionFile = open(os.path.join(wdir, "presets/{n}". format(n=filename)))
    solutionText = solutionFile.read()
    testText = testFile.read()
    if replace:
        solutionTextName = solutionText.replace(
            "Name", module[0].upper() + module[1:])
        solutionTextName = solutionTextName.replace("name", module)
    else:
        solutionTextName = solutionText
    assert solutionTextName == testText
    if replace:
        testText = testText.replace(module[0].upper() + module[1:], "Name")
        testText = testText.replace(module, "name")
    assert testText == solutionText
