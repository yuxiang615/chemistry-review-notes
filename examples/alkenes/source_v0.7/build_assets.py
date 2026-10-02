"""Archived regeneration logic from the v0.7 source package.
Run in the same directory as master_v0.7.tex; does not recreate the three course PNGs.
Source chemistry and all stereoisomeric products still require independent review.
"""
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
import os,cairosvg,sys
OUT=os.path.join(os.path.dirname(__file__),'assets')
os.makedirs(OUT,exist_ok=True)
M={
 'ethene':'C=C','propene':'CC=C','but1':'CCC=C','but2_cis':'C/C=C\\C','but2_trans':'C/C=C/C',
 'two_cl_but2_E':'C/C(Cl)=C\\C','two_cl_but2_Z':'C/C(Cl)=C/C',
 'isobutene':'C=C(C)C','pent1':'CCCC=C','pent2_E':'C/C=C/CC','pent2_Z':'C/C=C\\CC',
 'two_methyl_but1':'C=C(C)CC','two_methyl_pent2':'CC(C)=CCC',
 'vinyl_heptane':'CCCC(C=C)CCC','vinyl':'C=C','allyl':'C=CC',
 'methylcyclopent1':'CC1=CCCC1','methylcyclopent3':'C1=CC(C)CC1',
 'cyclohexene':'C1=CCCCC1','cyclopentene':'C1=CCCC1','methylcyclohexene':'CC1=CCCCC1',
 'cis_cycbut2':'C/C=C\\C',
 'butane':'CCCC','propane':'CCC','cyclohexdial':'O=CCCCCC=O','cyc_allyl_bromo':'BrC1C=CCCC1','hexadiene14':'CC=CCC=C','pentane':'CCCCC','isobutane':'CC(C)C',
 'but1_bromo':'CCCCBr','but2_bromo':'CCC(C)Br','prop2_bromo':'CC(C)Br','prop1_bromo':'CCCBr',
 'tertbutylbromide':'CC(C)(C)Br','isobutylbromide':'CC(C)CBr',
 'ethanol':'CCO','dibromoethane':'BrCCBr','propan2ol':'CC(C)O','propan1ol':'CCCO','butan2ol':'CCC(C)O','butan1ol':'CCCCO',
 'tertbutanol':'CC(C)(C)O','isobutanol':'CC(C)CO',
 'isopropyl_sulfate':'CC(C)OS(=O)(=O)O','ethyl_sulfate':'CCOS(=O)(=O)O','tertbutyl_sulfate':'CC(C)(C)OS(=O)(=O)O',
 'prop_dibromide':'CC(Br)CBr','but_dibromide':'CCC(Br)CBr','prop_bromohydrin':'CC(O)CBr',
 'isobutene_bromohydrin':'CC(C)(O)CBr','prop_diol':'CC(O)CO','but_diol':'CCC(O)CO',
 'ethanal':'CC=O','methanal':'C=O','propanal':'CCC=O','acetone':'CC(C)=O',
 'aceticacid':'CC(O)=O','propanoicacid':'CCC(O)=O',
 'propyleneoxide':'CC1CO1','cyclohexeneoxide':'C1CCC2OC2C1',
 'cyclohexane':'C1CCCCC1','cyclohexanol':'OC1CCCCC1',
 'cyc12diol_trans':'O[C@H]1CCCC[C@@H]1O','cyc12diol_cis':'O[C@H]1CCCC[C@H]1O',
 'cyc12dibromo_trans':'Br[C@H]1CCCC[C@@H]1Br',
 'cyc_bromohydrin_trans':'Br[C@H]1CCCC[C@@H]1O','cyc_bromomethoxy_trans':'Br[C@H]1CCCC[C@@H]1OC',
 'allyl_bromide':'C=CCBr','allyl_chloride':'C=CCCl',
 'two_methyl_but2':'CC=C(C)C',
 'two_methylpent2':'CC=C(C)CC',
 'spiro45':'C1CCC2(C1)CCCCC2',
 'decalin':'C1CCC2CCCCC2C1',
 'dimethylcycdiol_cis':'C[C@]1(O)CCC[C@@]1(C)O','dimethylcyclopent_epoxide':'C[C@]12CCC[C@@]1(C)O2','dimethylcyclopentene':'CC1=C(C)CCC1',
 'diketone_ringopen':'CC(=O)CCCC(=O)C',
 'butyne2':'CC#CC','butene2_cis':'C/C=C\\C',
 'butene2_trans':'C/C=C/C',
 'diol_meso':'C[C@H](O)[C@H](O)C',
 'but2_carbocation':'CCC[CH2+]',
 'prop_bromide':'CC(C)Br',
 'but2_alkene':'CC=CC',
 'bromo_2methylbut2':'CC(Br)(C)CC',
 'three_methylbut1':'C=CC(C)C',
 'two_methylbut2_ol':'CC(O)(C)CC',
 'butanone':'CCC(C)=O',
 'iodomethyl':'C(C)I',
 'methylenecyclopentane':'C=C1CCCC1',
 'one_methylcyclopentanol':'CC1(O)CCCC1',
 'cyclopentylmethanol':'OCC1CCCC1',
 'cyclopentylmethylbromide':'BrCC1CCCC1',
 'one_methylcyclopentyl_sulfate':'CC1(OS(=O)(=O)O)CCCC1',
 'isobutene_iodochloride':'CC(C)(Cl)CI',
 'adipic_acid':'O=C(O)CCCCC(=O)O',
 'one_methylcyclopentene':'CC1=CCCC1',
 'one_methylcycpent_transdibromide':'C[C@]1(Br)[C@H](Br)CCC1',
 'one_methylcycpent_cisdiol':'C[C@]1(O)[C@@H](O)CCC1',
 'one_methylcycpent_epoxide':'CC12CCCC1O2',
 'one_methylcycpent_bromohydrin':'C[C@]1(O)[C@H](Br)CCC1',
 'one_methylcychexene':'CC1=CCCCC1',
 'one_methylcychex_transdibromide':'C[C@]1(Br)[C@H](Br)CCCC1',
 'one_methylcychex_cisdiol':'C[C@]1(O)[C@@H](O)CCCC1',
 'one_methylcychex_epoxide':'CC12CCCCC1O2',
 'one_methylcychex_bromohydrin':'C[C@]1(O)[C@H](Br)CCCC1',
 'one_methylcychex_hydroborate':'C[C@H]1[C@H](O)CCCC1',
 'one_methylcychex_allylbr3':'CC1=CC(Br)CCC1',
 'one_methylcychex_bromomethyl':'BrCC1=CCCCC1',
 'one_methylcychex_allylbr6':'CC1=CCCCC1Br',
 'one_methylcychex_hbrperoxide':'CC1C(Br)CCCC1'
}
fail=[]
for name,smi in M.items():
 m=Chem.MolFromSmiles(smi)
 if not m:fail.append((name,smi));continue
 Chem.AssignStereochemistry(m,cleanIt=True,force=True)
 rdDepictor.Compute2DCoords(m)
 n=max(180,len(smi)*17)
 if name=='vinyl_heptane':n=285
 if name.startswith('one_methylcyc'):n=240
 if name.startswith(('spiro','diketone')):n=380
 if name.startswith('cyc12') or name.startswith('cyclohex'):n=300
 canvas=rdMolDraw2D.MolDraw2DSVG(n,190)
 opts=canvas.drawOptions()
 opts.useBWAtomPalette()
 opts.bondLineWidth=2.0
 opts.explicitMethyl=True
 opts.padding=0.11
 opts.minFontSize=15
 opts.maxFontSize=28
 opts.fixedFontSize=24 if name=="vinyl_heptane" else (22 if name.startswith("one_methylcyc") else 19)
 opts.additionalAtomLabelPadding=0.0
 canvas.DrawMolecule(m);canvas.FinishDrawing()
 svg=canvas.GetDrawingText()
 open(f'{OUT}/{name}.svg','w').write(svg)
 cairosvg.svg2pdf(bytestring=svg.encode(),write_to=f'{OUT}/{name}.pdf')
 print(name,smi,'stereo',[(b.GetIdx(),str(b.GetStereo())) for b in m.GetBonds() if b.GetBondType()==Chem.BondType.DOUBLE and b.GetStereo()!=Chem.BondStereo.STEREONONE])
if fail:raise ValueError(fail)
