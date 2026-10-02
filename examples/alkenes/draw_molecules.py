"""Minimal original RDKit black-and-white vector examples for this repository.
Checks depiction/format; does not verify unrelated reaction chemistry.
"""
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
import cairosvg

OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(exist_ok=True)
MOLECULES = {
    "but1": "CCC=C",
    "propene": "CC=C",
    "isopropyl_sulfate": "CC(C)OS(=O)(=O)O",
    "propan2ol": "CC(C)O",
    "bromohydrin": "CC(O)CBr",
}
for key, smiles in MOLECULES.items():
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Unparseable example: {key}={smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DSVG(330, 190)
    opts = drawer.drawOptions()
    opts.useBWAtomPalette()
    opts.bondLineWidth = 2.0
    opts.fixedFontSize = 22
    opts.explicitMethyl = True
    opts.padding = 0.1
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    (OUT / f"{key}.svg").write_text(svg, encoding="utf-8")
    cairosvg.svg2pdf(bytestring=svg.encode("utf-8"),
                     write_to=str(OUT / f"{key}.pdf"))
    print(f"generated {key}")
