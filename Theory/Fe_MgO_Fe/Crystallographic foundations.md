Crystallographic foundations for Fe/MgO/Fe
Scope
This lesson establishes the crystallographic information needed before constructing a Fe/MgO/Fe magnetic tunnel junction (MTJ) in QuantumATK. It combines basic crystallography with the first Builder tasks. No DFT or NEGF calculation is performed today.
1. Lattice, basis, crystal, and unit cell
A crystal is a periodic arrangement of atoms or ions.
- Lattice: a periodic set of geometrical points.
- Basis (motif): the atom or group of atoms associated with each lattice point.
- Crystal structure: the lattice together with its basis.
- Unit cell: a volume that reproduces the crystal by translations.
Crystal structure = Lattice + Basis

A unit cell is defined by three lattice vectors, conventionally called a, b, and c, and three angles, α, β, and γ. For a cubic cell:

a = b = c; α = β = γ = 90°

The edge length is the lattice parameter. It is not necessarily equal to the nearest-neighbour distance.

1 Å = 10⁻¹⁰ m

A conventional cell makes the symmetry easy to see, while a primitive cell is the smallest cell that contains exactly one lattice point. The number of atoms in the two cell choices can therefore differ without changing the underlying crystal.
2. Alpha-iron: BCC
At room temperature and ambient pressure, alpha-iron (α-Fe) has a body-centred cubic (BCC) crystal structure. Its space group is Im3̅m (No. 229).

In the conventional cubic description, the lattice points are located at the eight corners and at the body centre. The effective atom count is

N = 8 × (1/8) + 1 = 2

Thus, a conventional BCC cell contains two Fe atoms. A primitive BCC cell contains one lattice point (one Fe atom).
Property	Alpha-Fe
Crystal structure	BCC
Space group	Im3̅m, No. 229
Lattice parameter near 25 °C	about 2.8665 Å
Atoms per conventional cell	2 Fe
Nearest-neighbour coordination number	8


The nearest-neighbour distance is half the body diagonal:

d₍Fe–Fe₎ = (√3 / 2) × a

For a = 2.8665 Å:

d₍Fe–Fe₎ ≈ 2.482 Å

Do not confuse the BCC conventional-cell edge a with the nearest-neighbour distance.
3. Magnesium oxide: rock-salt structure
MgO crystallizes in the rock-salt (NaCl-type) structure. It has an FCC Bravais lattice and a two-ion basis. A simple ionic picture describes the ions as Mg²⁺ and O²⁻.

The conventional cubic cell contains four Mg ions and four O ions, i.e. four MgO formula units.
Property	MgO
Crystal structure	Rock salt (NaCl type)
Bravais lattice	FCC
Space group	Fm3̅m, No. 225
Lattice parameter at 298 K	4.21154 Å
Ions per conventional cell	4 Mg + 4 O
Formula units per conventional cell	4
Coordination number	6 for Mg and 6 for O


Each Mg ion has six nearest-neighbour O ions, and each O ion has six nearest-neighbour Mg ions. The coordination is octahedral.
4. Planes and directions: (001) and [001]
Miller indices describe crystallographic planes and directions:
- (001): a plane.
- [001]: a direction.
For a cubic crystal, [001] is perpendicular to the (001) plane. In a typical Fe(001)/MgO(001)/Fe(001) junction, the interface is parallel to the (001) planes and electron transport is along the direction normal to the interface.

For the device coordinate system, think of x and y as directions in the interface plane and z as the direction perpendicular to the interface and along transport.
5. Why Fe and MgO need an interface-matching procedure
A commonly used epitaxial relationship is

Fe(001) ∥ MgO(001)
Fe[100] ∥ MgO[110]

This corresponds to a 45-degree in-plane rotation. In this matching geometry, the Fe in-plane repeat length is compared with the MgO surface repeat length along [110]:

a₍Fe₎ ≈ 2.8665 Å

a₍MgO₎ / √2 ≈ 2.9780 Å

A mismatch of roughly 3.9% is obtained when the Fe value is used as the reference. The numerical percentage depends on the convention used in the denominator. The mismatch means that strain and atomic relaxation need to be considered when constructing the coherent interface. This will be studied on Day 02; do not impose a strain choice yet.
6. QuantumATK 2016.4 — Day 01 Builder practice
A. Load alpha-Fe from the crystal database
1. Open QuantumATK 2016.4 and create or open the learning project.
2. Open Builder.
3. In the Builder Stash, select Add → From Database.
4. Select the Crystals database tab.
5. Search for Iron or Iron (alpha).
6. Select the alpha-iron BCC entry and add it to the Stash.
7. Inspect the 3D structure. Rotate, zoom, and identify the cubic cell.
If the database entry is represented using a primitive cell, it may contain one Fe atom. If it is represented using the conventional BCC cell, it contains two Fe atoms. Both can describe the same bulk crystal.
B. Check the crystal symmetry
1. Activate the Fe structure in the Stash.
2. Open Bulk Tools → Crystal Symmetry Info.
3. Use Detect.
4. Check that the result is consistent with BCC alpha-Fe and space group Im3̅m (No. 229).
5. Inspect the lattice parameters and atom count.
C. Load MgO from the crystal database
Repeat the database workflow and search for MgO or Magnesium Oxide. Confirm that the structure is rock salt, with a 1:1 Mg:O ratio and FCC-based symmetry. A conventional cell has 8 ions (4 Mg and 4 O); a primitive cell can contain 2 ions (1 Mg and 1 O).
D. If a material is not available in the database
QuantumATK 2016.0 documentation describes the Crystal Builder plugin at:

Add → From Plugin → Crystal Builder

It creates a bulk crystal from its space group, lattice parameters, and atomic (Wyckoff) positions. Use the crystallographic data above as a guide, but check the exact fields and generated atom count before saving. For the first attempt, database import is preferred because it reduces the chance of entering incorrect fractional coordinates.
E. Save the structures
Save the two configurations separately, with clear names such as:
- Fe_alpha_bulk.nc
- MgO_rocksalt_bulk.nc
Keep the original database structures unchanged. Do not combine the two materials yet.
7. What to record from QuantumATK
Complete this table after loading the structures:
Item	Fe	MgO
Database entry name		
Crystal structure		
Space group reported		
Lattice parameters (Å)		
Number of atoms in the imported cell		
Primitive or conventional cell		
Symmetry detection successful?		


The imported atom count may differ depending on whether the database provides a primitive or conventional cell. Record what QuantumATK actually shows rather than forcing the count to match the conventional-cell values.
8. Self-check questions
1. What is the difference between a lattice and a basis?
2. Why does a conventional BCC cell contain two Fe atoms?
3. How many MgO formula units are in the conventional rock-salt cell?
4. What is the coordination number of Mg in MgO?
5. What is the difference between (001) and [001]?
6. Why is a 45-degree in-plane relationship used when matching Fe(001) and MgO(001)?
7. Why can a primitive Fe cell contain one atom even though the conventional BCC cell contains two?
9. What we should achieve today
- Understand the BCC structure of alpha-Fe.
- Understand the rock-salt structure of MgO.
- Distinguish primitive and conventional unit cells.
- Recognize (001) planes and [001] directions.
- Load Fe and MgO separately in QuantumATK.
- Verify the crystal symmetry and record the lattice parameters.
- Save both bulk configurations for later surface and interface construction.
No DFT, geometry optimization, device construction, or NEGF transport calculation is required on Day 01.
References and documentation
1. QuantumATK, Spin transport in magnetic tunnel junctions, Version 2016.0: https://docs.quantumatk.com/tutorials/fe_mgo_fe/fe_mgo_fe.html
2. QuantumATK, Using the Crystal Builder, Version 2016.0: https://docs.quantumatk.com/guides/crystal_builder/crystal_builder.html
3. QuantumATK, Overview of built-in Builder plugins: https://docs.quantumatk.com/guides/builder_manual/builder_plugins/builder_plugins.html
4. AIST, crystal structure data for iron at 25 °C: https://unit.aist.go.jp/mmri/ja/organization/db-nomura/common/struc-coord/Fe-c.html
5. NIST Ceramics Data Portal, MgO lattice parameter at 298 K: https://srdata.nist.gov/CeramicDataPortal/Scd/Z00631
Next: 
Fe/MgO/Fe geometry, the roles of the electrodes and barrier, interface orientation, lattice matching, strain, and monolayer thickness.
