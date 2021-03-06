# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from enum import Enum

from pkg_resources import parse_version

from ...vendor.kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO

if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))


class MachO(KaitaiStruct):
    class MagicType(Enum):
        fat_le = 3199925962
        fat_be = 3405691582
        macho_le_x86 = 3472551422
        macho_le_x64 = 3489328638
        macho_be_x86 = 4277009102
        macho_be_x64 = 4277009103

    class CpuType(Enum):
        vax = 1
        romp = 2
        ns32032 = 4
        ns32332 = 5
        i386 = 7
        mips = 8
        ns32532 = 9
        hppa = 11
        arm = 12
        mc88000 = 13
        sparc = 14
        i860 = 15
        i860_little = 16
        rs6000 = 17
        powerpc = 18
        abi64 = 16777216
        x86_64 = 16777223
        arm64 = 16777228
        powerpc64 = 16777234
        any = 4294967295

    class FileType(Enum):
        object = 1
        execute = 2
        fvmlib = 3
        core = 4
        preload = 5
        dylib = 6
        dylinker = 7
        bundle = 8
        dylib_stub = 9
        dsym = 10
        kext_bundle = 11

    class LoadCommandType(Enum):
        segment = 1
        symtab = 2
        symseg = 3
        thread = 4
        unix_thread = 5
        load_fvm_lib = 6
        id_fvm_lib = 7
        ident = 8
        fvm_file = 9
        prepage = 10
        dysymtab = 11
        load_dylib = 12
        id_dylib = 13
        load_dylinker = 14
        id_dylinker = 15
        prebound_dylib = 16
        routines = 17
        sub_framework = 18
        sub_umbrella = 19
        sub_client = 20
        sub_library = 21
        twolevel_hints = 22
        prebind_cksum = 23
        segment_64 = 25
        routines_64 = 26
        uuid = 27
        code_signature = 29
        segment_split_info = 30
        lazy_load_dylib = 32
        encryption_info = 33
        dyld_info = 34
        version_min_macosx = 36
        version_min_iphoneos = 37
        function_starts = 38
        dyld_environment = 39
        data_in_code = 41
        source_version = 42
        dylib_code_sign_drs = 43
        encryption_info_64 = 44
        linker_option = 45
        linker_optimization_hint = 46
        version_min_tvos = 47
        version_min_watchos = 48
        req_dyld = 2147483648
        load_weak_dylib = 2147483672
        rpath = 2147483676
        reexport_dylib = 2147483679
        dyld_info_only = 2147483682
        load_upward_dylib = 2147483683
        main = 2147483688

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._root.MagicType(self._io.read_u4be())
        self.header = self._root.MachHeader(self._io, self, self._root)
        self.load_commands = [None] * (self.header.ncmds)
        for i in range(self.header.ncmds):
            self.load_commands[i] = self._root.LoadCommand(self._io, self, self._root)

    class RpathCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.path_offset = self._io.read_u4le()
            self.path = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")

    class Uleb128(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b1 = self._io.read_u1()
            if (self.b1 & 128) != 0:
                self.b2 = self._io.read_u1()

            if (self.b2 & 128) != 0:
                self.b3 = self._io.read_u1()

            if (self.b3 & 128) != 0:
                self.b4 = self._io.read_u1()

            if (self.b4 & 128) != 0:
                self.b5 = self._io.read_u1()

            if (self.b5 & 128) != 0:
                self.b6 = self._io.read_u1()

            if (self.b6 & 128) != 0:
                self.b7 = self._io.read_u1()

            if (self.b7 & 128) != 0:
                self.b8 = self._io.read_u1()

            if (self.b8 & 128) != 0:
                self.b9 = self._io.read_u1()

            if (self.b9 & 128) != 0:
                self.b10 = self._io.read_u1()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (((self.b1 % 128) << 0) + (0 if (self.b1 & 128) == 0 else (((self.b2 % 128) << 7) + (
                0 if (self.b2 & 128) == 0 else (((self.b3 % 128) << 14) + (0 if (self.b3 & 128) == 0 else (
                        ((self.b4 % 128) << 21) + (0 if (self.b4 & 128) == 0 else (((self.b5 % 128) << 28) + (
                    0 if (self.b5 & 128) == 0 else (((self.b6 % 128) << 35) + (0 if (self.b6 & 128) == 0 else (
                            ((self.b7 % 128) << 42) + (0 if (self.b7 & 128) == 0 else (
                            ((self.b8 % 128) << 49) + (0 if (self.b8 & 128) == 0 else (
                            ((self.b9 % 128) << 56) + (
                        0 if (self.b8 & 128) == 0 else ((self.b10 % 128) << 63)))))))))))))))))))
            return self._m_value if hasattr(self, '_m_value') else None

    class SourceVersionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u8le()

    class CsBlob(KaitaiStruct):

        class CsMagic(Enum):
            blob_wrapper = 4208855809
            requirement = 4208856064
            requirements = 4208856065
            code_directory = 4208856066
            embedded_signature = 4208856256
            detached_signature = 4208856257
            entitlement = 4208882033

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._root.CsBlob.CsMagic(self._io.read_u4be())
            self.length = self._io.read_u4be()
            _on = self.magic
            if _on == self._root.CsBlob.CsMagic.detached_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.SuperBlob(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.embedded_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.SuperBlob(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.entitlement:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Entitlement(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.blob_wrapper:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.BlobWrapper(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.requirement:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Requirement(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.code_directory:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.CodeDirectory(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.requirements:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Requirements(io, self, self._root)
            else:
                self.body = self._io.read_bytes((self.length - 8))

        class Entitlement(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes_full()

        class CodeDirectory(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.version = self._io.read_u4be()
                self.flags = self._io.read_u4be()
                self.hash_offset = self._io.read_u4be()
                self.ident_offset = self._io.read_u4be()
                self.n_special_slots = self._io.read_u4be()
                self.n_code_slots = self._io.read_u4be()
                self.code_limit = self._io.read_u4be()
                self.hash_size = self._io.read_u1()
                self.hash_type = self._io.read_u1()
                self.spare1 = self._io.read_u1()
                self.page_size = self._io.read_u1()
                self.spare2 = self._io.read_u4be()
                if self.version >= 131328:
                    self.scatter_offset = self._io.read_u4be()

                if self.version >= 131584:
                    self.team_id_offset = self._io.read_u4be()

            @property
            def ident(self):
                if hasattr(self, '_m_ident'):
                    return self._m_ident if hasattr(self, '_m_ident') else None

                _pos = self._io.pos()
                self._io.seek((self.ident_offset - 8))
                self._m_ident = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return self._m_ident if hasattr(self, '_m_ident') else None

            @property
            def team_id(self):
                if hasattr(self, '_m_team_id'):
                    return self._m_team_id if hasattr(self, '_m_team_id') else None

                _pos = self._io.pos()
                self._io.seek((self.team_id_offset - 8))
                self._m_team_id = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return self._m_team_id if hasattr(self, '_m_team_id') else None

            @property
            def hashes(self):
                if hasattr(self, '_m_hashes'):
                    return self._m_hashes if hasattr(self, '_m_hashes') else None

                _pos = self._io.pos()
                self._io.seek(((self.hash_offset - 8) - (self.hash_size * self.n_special_slots)))
                self._m_hashes = [None] * ((self.n_special_slots + self.n_code_slots))
                for i in range((self.n_special_slots + self.n_code_slots)):
                    self._m_hashes[i] = self._io.read_bytes(self.hash_size)

                self._io.seek(_pos)
                return self._m_hashes if hasattr(self, '_m_hashes') else None

        class Data(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.length = self._io.read_u4be()
                self.value = self._io.read_bytes(self.length)
                self.padding = self._io.read_bytes((4 - (self.length & 3)))

        class SuperBlob(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.count = self._io.read_u4be()
                self.blobs = [None] * (self.count)
                for i in range(self.count):
                    self.blobs[i] = self._root.CsBlob.BlobIndex(self._io, self, self._root)

        class Expr(KaitaiStruct):

            class OpEnum(Enum):
                false = 0
                true = 1
                ident = 2
                apple_anchor = 3
                anchor_hash = 4
                info_key_value = 5
                and_op = 6
                or_op = 7
                cd_hash = 8
                not_op = 9
                info_key_field = 10
                cert_field = 11
                trusted_cert = 12
                trusted_certs = 13
                cert_generic = 14
                apple_generic_anchor = 15
                entitlement_field = 16

            class CertSlot(Enum):
                left_cert = 0
                anchor_cert = 4294967295

            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.op = self._root.CsBlob.Expr.OpEnum(self._io.read_u4be())
                _on = self.op
                if _on == self._root.CsBlob.Expr.OpEnum.cert_generic:
                    self.data = self._root.CsBlob.Expr.CertGenericExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.apple_generic_anchor:
                    self.data = self._root.CsBlob.Expr.AppleGenericAnchorExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.info_key_field:
                    self.data = self._root.CsBlob.Expr.InfoKeyFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.and_op:
                    self.data = self._root.CsBlob.Expr.AndExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.anchor_hash:
                    self.data = self._root.CsBlob.Expr.AnchorHashExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.info_key_value:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.or_op:
                    self.data = self._root.CsBlob.Expr.OrExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.trusted_cert:
                    self.data = self._root.CsBlob.Expr.CertSlotExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.not_op:
                    self.data = self._root.CsBlob.Expr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.ident:
                    self.data = self._root.CsBlob.Expr.IdentExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.cert_field:
                    self.data = self._root.CsBlob.Expr.CertFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.entitlement_field:
                    self.data = self._root.CsBlob.Expr.EntitlementFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.cd_hash:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)

            class InfoKeyFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)

            class CertSlotExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.value = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())

            class CertGenericExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)

            class IdentExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.identifier = self._root.CsBlob.Data(self._io, self, self._root)

            class CertFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)

            class AnchorHashExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)

            class AppleGenericAnchorExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    pass

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value if hasattr(self, '_m_value') else None

                    self._m_value = u"anchor apple generic"
                    return self._m_value if hasattr(self, '_m_value') else None

            class EntitlementFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)

            class AndExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.left = self._root.CsBlob.Expr(self._io, self, self._root)
                    self.right = self._root.CsBlob.Expr(self._io, self, self._root)

            class OrExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.left = self._root.CsBlob.Expr(self._io, self, self._root)
                    self.right = self._root.CsBlob.Expr(self._io, self, self._root)

        class BlobIndex(KaitaiStruct):

            class CsslotType(Enum):
                code_directory = 0
                info_slot = 1
                requirements = 2
                resource_dir = 3
                application = 4
                entitlements = 5
                alternate_code_directories = 4096
                signature_slot = 65536

            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.type = self._root.CsBlob.BlobIndex.CsslotType(self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def blob(self):
                if hasattr(self, '_m_blob'):
                    return self._m_blob if hasattr(self, '_m_blob') else None

                io = self._parent._io
                _pos = io.pos()
                io.seek((self.offset - 8))
                self._raw__m_blob = io.read_bytes_full()
                io = KaitaiStream(BytesIO(self._raw__m_blob))
                self._m_blob = self._root.CsBlob(io, self, self._root)
                io.seek(_pos)
                return self._m_blob if hasattr(self, '_m_blob') else None

        class Match(KaitaiStruct):

            class Op(Enum):
                exists = 0
                equal = 1
                contains = 2
                begins_with = 3
                ends_with = 4
                less_than = 5
                greater_than = 6
                less_equal = 7
                greater_equal = 8

            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.match_op = self._root.CsBlob.Match.Op(self._io.read_u4be())
                if self.match_op != self._root.CsBlob.Match.Op.exists:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)

        class Requirement(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.kind = self._io.read_u4be()
                self.expr = self._root.CsBlob.Expr(self._io, self, self._root)

        class Requirements(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.count = self._io.read_u4be()
                self.items = [None] * (self.count)
                for i in range(self.count):
                    self.items[i] = self._root.CsBlob.RequirementsBlobIndex(self._io, self, self._root)

        class BlobWrapper(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes_full()

        class RequirementsBlobIndex(KaitaiStruct):

            class RequirementType(Enum):
                host = 1
                guest = 2
                designated = 3
                library = 4

            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.type = self._root.CsBlob.RequirementsBlobIndex.RequirementType(self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value if hasattr(self, '_m_value') else None

                _pos = self._io.pos()
                self._io.seek((self.offset - 8))
                self._m_value = self._root.CsBlob(self._io, self, self._root)
                self._io.seek(_pos)
                return self._m_value if hasattr(self, '_m_value') else None

    class RoutinesCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.init_address = self._io.read_u4le()
            self.init_module = self._io.read_u4le()
            self.reserved = self._io.read_bytes(24)

    class MachoFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def subsections_via_symbols(self):
            """safe to divide up the sections into sub-sections via symbols for dead code stripping."""
            if hasattr(self, '_m_subsections_via_symbols'):
                return self._m_subsections_via_symbols if hasattr(self, '_m_subsections_via_symbols') else None

            self._m_subsections_via_symbols = (self.value & 8192) != 0
            return self._m_subsections_via_symbols if hasattr(self, '_m_subsections_via_symbols') else None

        @property
        def dead_strippable_dylib(self):
            if hasattr(self, '_m_dead_strippable_dylib'):
                return self._m_dead_strippable_dylib if hasattr(self, '_m_dead_strippable_dylib') else None

            self._m_dead_strippable_dylib = (self.value & 4194304) != 0
            return self._m_dead_strippable_dylib if hasattr(self, '_m_dead_strippable_dylib') else None

        @property
        def weak_defines(self):
            """the final linked image contains external weak symbols."""
            if hasattr(self, '_m_weak_defines'):
                return self._m_weak_defines if hasattr(self, '_m_weak_defines') else None

            self._m_weak_defines = (self.value & 32768) != 0
            return self._m_weak_defines if hasattr(self, '_m_weak_defines') else None

        @property
        def prebound(self):
            """the file has its dynamic undefined references prebound."""
            if hasattr(self, '_m_prebound'):
                return self._m_prebound if hasattr(self, '_m_prebound') else None

            self._m_prebound = (self.value & 16) != 0
            return self._m_prebound if hasattr(self, '_m_prebound') else None

        @property
        def all_mods_bound(self):
            """indicates that this binary binds to all two-level namespace modules of its dependent libraries. only used when MH_PREBINDABLE and MH_TWOLEVEL are both set."""
            if hasattr(self, '_m_all_mods_bound'):
                return self._m_all_mods_bound if hasattr(self, '_m_all_mods_bound') else None

            self._m_all_mods_bound = (self.value & 4096) != 0
            return self._m_all_mods_bound if hasattr(self, '_m_all_mods_bound') else None

        @property
        def has_tlv_descriptors(self):
            if hasattr(self, '_m_has_tlv_descriptors'):
                return self._m_has_tlv_descriptors if hasattr(self, '_m_has_tlv_descriptors') else None

            self._m_has_tlv_descriptors = (self.value & 8388608) != 0
            return self._m_has_tlv_descriptors if hasattr(self, '_m_has_tlv_descriptors') else None

        @property
        def force_flat(self):
            """the executable is forcing all images to use flat name space bindings."""
            if hasattr(self, '_m_force_flat'):
                return self._m_force_flat if hasattr(self, '_m_force_flat') else None

            self._m_force_flat = (self.value & 256) != 0
            return self._m_force_flat if hasattr(self, '_m_force_flat') else None

        @property
        def root_safe(self):
            """When this bit is set, the binary declares it is safe for use in processes with uid zero."""
            if hasattr(self, '_m_root_safe'):
                return self._m_root_safe if hasattr(self, '_m_root_safe') else None

            self._m_root_safe = (self.value & 262144) != 0
            return self._m_root_safe if hasattr(self, '_m_root_safe') else None

        @property
        def no_undefs(self):
            """the object file has no undefined references."""
            if hasattr(self, '_m_no_undefs'):
                return self._m_no_undefs if hasattr(self, '_m_no_undefs') else None

            self._m_no_undefs = (self.value & 1) != 0
            return self._m_no_undefs if hasattr(self, '_m_no_undefs') else None

        @property
        def setuid_safe(self):
            """When this bit is set, the binary declares it is safe for use in processes when issetugid() is true."""
            if hasattr(self, '_m_setuid_safe'):
                return self._m_setuid_safe if hasattr(self, '_m_setuid_safe') else None

            self._m_setuid_safe = (self.value & 524288) != 0
            return self._m_setuid_safe if hasattr(self, '_m_setuid_safe') else None

        @property
        def no_heap_execution(self):
            if hasattr(self, '_m_no_heap_execution'):
                return self._m_no_heap_execution if hasattr(self, '_m_no_heap_execution') else None

            self._m_no_heap_execution = (self.value & 16777216) != 0
            return self._m_no_heap_execution if hasattr(self, '_m_no_heap_execution') else None

        @property
        def no_reexported_dylibs(self):
            """When this bit is set on a dylib, the static linker does not need to examine dependent dylibs to see if any are re-exported."""
            if hasattr(self, '_m_no_reexported_dylibs'):
                return self._m_no_reexported_dylibs if hasattr(self, '_m_no_reexported_dylibs') else None

            self._m_no_reexported_dylibs = (self.value & 1048576) != 0
            return self._m_no_reexported_dylibs if hasattr(self, '_m_no_reexported_dylibs') else None

        @property
        def no_multi_defs(self):
            """this umbrella guarantees no multiple defintions of symbols in its sub-images so the two-level namespace hints can always be used."""
            if hasattr(self, '_m_no_multi_defs'):
                return self._m_no_multi_defs if hasattr(self, '_m_no_multi_defs') else None

            self._m_no_multi_defs = (self.value & 512) != 0
            return self._m_no_multi_defs if hasattr(self, '_m_no_multi_defs') else None

        @property
        def app_extension_safe(self):
            if hasattr(self, '_m_app_extension_safe'):
                return self._m_app_extension_safe if hasattr(self, '_m_app_extension_safe') else None

            self._m_app_extension_safe = (self.value & 33554432) != 0
            return self._m_app_extension_safe if hasattr(self, '_m_app_extension_safe') else None

        @property
        def prebindable(self):
            """the binary is not prebound but can have its prebinding redone. only used when MH_PREBOUND is not set."""
            if hasattr(self, '_m_prebindable'):
                return self._m_prebindable if hasattr(self, '_m_prebindable') else None

            self._m_prebindable = (self.value & 2048) != 0
            return self._m_prebindable if hasattr(self, '_m_prebindable') else None

        @property
        def incr_link(self):
            """the object file is the output of an incremental link against a base file and can't be link edited again."""
            if hasattr(self, '_m_incr_link'):
                return self._m_incr_link if hasattr(self, '_m_incr_link') else None

            self._m_incr_link = (self.value & 2) != 0
            return self._m_incr_link if hasattr(self, '_m_incr_link') else None

        @property
        def bind_at_load(self):
            """the object file's undefined references are bound by the dynamic linker when loaded."""
            if hasattr(self, '_m_bind_at_load'):
                return self._m_bind_at_load if hasattr(self, '_m_bind_at_load') else None

            self._m_bind_at_load = (self.value & 8) != 0
            return self._m_bind_at_load if hasattr(self, '_m_bind_at_load') else None

        @property
        def canonical(self):
            """the binary has been canonicalized via the unprebind operation."""
            if hasattr(self, '_m_canonical'):
                return self._m_canonical if hasattr(self, '_m_canonical') else None

            self._m_canonical = (self.value & 16384) != 0
            return self._m_canonical if hasattr(self, '_m_canonical') else None

        @property
        def two_level(self):
            """the image is using two-level name space bindings."""
            if hasattr(self, '_m_two_level'):
                return self._m_two_level if hasattr(self, '_m_two_level') else None

            self._m_two_level = (self.value & 128) != 0
            return self._m_two_level if hasattr(self, '_m_two_level') else None

        @property
        def split_segs(self):
            """the file has its read-only and read-write segments split."""
            if hasattr(self, '_m_split_segs'):
                return self._m_split_segs if hasattr(self, '_m_split_segs') else None

            self._m_split_segs = (self.value & 32) != 0
            return self._m_split_segs if hasattr(self, '_m_split_segs') else None

        @property
        def lazy_init(self):
            """the shared library init routine is to be run lazily via catching memory faults to its writeable segments (obsolete)."""
            if hasattr(self, '_m_lazy_init'):
                return self._m_lazy_init if hasattr(self, '_m_lazy_init') else None

            self._m_lazy_init = (self.value & 64) != 0
            return self._m_lazy_init if hasattr(self, '_m_lazy_init') else None

        @property
        def allow_stack_execution(self):
            """When this bit is set, all stacks in the task will be given stack execution privilege.  Only used in MH_EXECUTE filetypes."""
            if hasattr(self, '_m_allow_stack_execution'):
                return self._m_allow_stack_execution if hasattr(self, '_m_allow_stack_execution') else None

            self._m_allow_stack_execution = (self.value & 131072) != 0
            return self._m_allow_stack_execution if hasattr(self, '_m_allow_stack_execution') else None

        @property
        def binds_to_weak(self):
            """the final linked image uses weak symbols."""
            if hasattr(self, '_m_binds_to_weak'):
                return self._m_binds_to_weak if hasattr(self, '_m_binds_to_weak') else None

            self._m_binds_to_weak = (self.value & 65536) != 0
            return self._m_binds_to_weak if hasattr(self, '_m_binds_to_weak') else None

        @property
        def no_fix_prebinding(self):
            """do not have dyld notify the prebinding agent about this executable."""
            if hasattr(self, '_m_no_fix_prebinding'):
                return self._m_no_fix_prebinding if hasattr(self, '_m_no_fix_prebinding') else None

            self._m_no_fix_prebinding = (self.value & 1024) != 0
            return self._m_no_fix_prebinding if hasattr(self, '_m_no_fix_prebinding') else None

        @property
        def dyld_link(self):
            """the object file is input for the dynamic linker and can't be staticly link edited again."""
            if hasattr(self, '_m_dyld_link'):
                return self._m_dyld_link if hasattr(self, '_m_dyld_link') else None

            self._m_dyld_link = (self.value & 4) != 0
            return self._m_dyld_link if hasattr(self, '_m_dyld_link') else None

        @property
        def pie(self):
            """When this bit is set, the OS will load the main executable at a random address. Only used in MH_EXECUTE filetypes."""
            if hasattr(self, '_m_pie'):
                return self._m_pie if hasattr(self, '_m_pie') else None

            self._m_pie = (self.value & 2097152) != 0
            return self._m_pie if hasattr(self, '_m_pie') else None

    class RoutinesCommand64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.init_address = self._io.read_u8le()
            self.init_module = self._io.read_u8le()
            self.reserved = self._io.read_bytes(48)

    class LinkerOptionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_strings = self._io.read_u4le()
            self.strings = [None] * (self.num_strings)
            for i in range(self.num_strings):
                self.strings[i] = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")

    class SegmentCommand64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.segname = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
            self.vmaddr = self._io.read_u8le()
            self.vmsize = self._io.read_u8le()
            self.fileoff = self._io.read_u8le()
            self.filesize = self._io.read_u8le()
            self.maxprot = self._root.VmProt(self._io, self, self._root)
            self.initprot = self._root.VmProt(self._io, self, self._root)
            self.nsects = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.sections = [None] * (self.nsects)
            for i in range(self.nsects):
                self.sections[i] = self._root.SegmentCommand64.Section64(self._io, self, self._root)

        class Section64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sect_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.seg_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.addr = self._io.read_u8le()
                self.size = self._io.read_u8le()
                self.offset = self._io.read_u4le()
                self.align = self._io.read_u4le()
                self.reloff = self._io.read_u4le()
                self.nreloc = self._io.read_u4le()
                self.flags = self._io.read_u4le()
                self.reserved1 = self._io.read_u4le()
                self.reserved2 = self._io.read_u4le()
                self.reserved3 = self._io.read_u4le()

            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data if hasattr(self, '_m_data') else None

                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset)
                self._m_data = io.read_bytes(self.size)
                io.seek(_pos)
                return self._m_data if hasattr(self, '_m_data') else None

    class VmProt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.strip_read = self._io.read_bits_int(1) != 0
            self.is_mask = self._io.read_bits_int(1) != 0
            self.reserved0 = self._io.read_bits_int(1) != 0
            self.copy = self._io.read_bits_int(1) != 0
            self.no_change = self._io.read_bits_int(1) != 0
            self.execute = self._io.read_bits_int(1) != 0
            self.write = self._io.read_bits_int(1) != 0
            self.read = self._io.read_bits_int(1) != 0
            self.reserved1 = self._io.read_bits_int(24)

    class DysymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.i_local_sym = self._io.read_u4le()
            self.n_local_sym = self._io.read_u4le()
            self.i_ext_def_sym = self._io.read_u4le()
            self.n_ext_def_sym = self._io.read_u4le()
            self.i_undef_sym = self._io.read_u4le()
            self.n_undef_sym = self._io.read_u4le()
            self.toc_off = self._io.read_u4le()
            self.n_toc = self._io.read_u4le()
            self.mod_tab_off = self._io.read_u4le()
            self.n_mod_tab = self._io.read_u4le()
            self.ext_ref_sym_off = self._io.read_u4le()
            self.n_ext_ref_syms = self._io.read_u4le()
            self.indirect_sym_off = self._io.read_u4le()
            self.n_indirect_syms = self._io.read_u4le()
            self.ext_rel_off = self._io.read_u4le()
            self.n_ext_rel = self._io.read_u4le()
            self.loc_rel_off = self._io.read_u4le()
            self.n_loc_rel = self._io.read_u4le()

        @property
        def indirect_symbols(self):
            if hasattr(self, '_m_indirect_symbols'):
                return self._m_indirect_symbols if hasattr(self, '_m_indirect_symbols') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.indirect_sym_off)
            self._m_indirect_symbols = [None] * (self.n_indirect_syms)
            for i in range(self.n_indirect_syms):
                self._m_indirect_symbols[i] = io.read_u4le()

            io.seek(_pos)
            return self._m_indirect_symbols if hasattr(self, '_m_indirect_symbols') else None

    class MachHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cputype = self._root.CpuType(self._io.read_u4le())
            self.cpusubtype = self._io.read_u4le()
            self.filetype = self._root.FileType(self._io.read_u4le())
            self.ncmds = self._io.read_u4le()
            self.sizeofcmds = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            if ((self._root.magic == self._root.MagicType.macho_be_x64) or (
                    self._root.magic == self._root.MagicType.macho_le_x64)):
                self.reserved = self._io.read_u4le()

        @property
        def flags_obj(self):
            if hasattr(self, '_m_flags_obj'):
                return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None

            self._m_flags_obj = self._root.MachoFlags(self.flags, self._io, self, self._root)
            return self._m_flags_obj if hasattr(self, '_m_flags_obj') else None

    class LinkeditDataCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()

    class SubCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = self._root.LcStr(self._io, self, self._root)

    class TwolevelHintsCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset = self._io.read_u4le()
            self.num_hints = self._io.read_u4le()

    class Version(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.p1 = self._io.read_u1()
            self.minor = self._io.read_u1()
            self.major = self._io.read_u1()
            self.release = self._io.read_u1()

    class EncryptionInfoCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cryptoff = self._io.read_u4le()
            self.cryptsize = self._io.read_u4le()
            self.cryptid = self._io.read_u4le()
            if ((self._root.magic == self._root.MagicType.macho_be_x64) or (
                    self._root.magic == self._root.MagicType.macho_le_x64)):
                self.pad = self._io.read_u4le()

    class CodeSignatureCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()

        @property
        def code_signature(self):
            if hasattr(self, '_m_code_signature'):
                return self._m_code_signature if hasattr(self, '_m_code_signature') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.data_off)
            self._raw__m_code_signature = io.read_bytes(self.data_size)
            io = KaitaiStream(BytesIO(self._raw__m_code_signature))
            self._m_code_signature = self._root.CsBlob(io, self, self._root)
            io.seek(_pos)
            return self._m_code_signature if hasattr(self, '_m_code_signature') else None

    class DyldInfoCommand(KaitaiStruct):

        class BindOpcode(Enum):
            done = 0
            set_dylib_ordinal_immediate = 16
            set_dylib_ordinal_uleb = 32
            set_dylib_special_immediate = 48
            set_symbol_trailing_flags_immediate = 64
            set_type_immediate = 80
            set_append_sleb = 96
            set_segment_and_offset_uleb = 112
            add_address_uleb = 128
            do_bind = 144
            do_bind_add_address_uleb = 160
            do_bind_add_address_immediate_scaled = 176
            do_bind_uleb_times_skipping_uleb = 192

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rebase_off = self._io.read_u4le()
            self.rebase_size = self._io.read_u4le()
            self.bind_off = self._io.read_u4le()
            self.bind_size = self._io.read_u4le()
            self.weak_bind_off = self._io.read_u4le()
            self.weak_bind_size = self._io.read_u4le()
            self.lazy_bind_off = self._io.read_u4le()
            self.lazy_bind_size = self._io.read_u4le()
            self.export_off = self._io.read_u4le()
            self.export_size = self._io.read_u4le()

        class BindItem(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.opcode_and_immediate = self._io.read_u1()
                if ((self.opcode == self._root.DyldInfoCommand.BindOpcode.set_dylib_ordinal_uleb) or (
                        self.opcode == self._root.DyldInfoCommand.BindOpcode.set_append_sleb) or (
                        self.opcode == self._root.DyldInfoCommand.BindOpcode.set_segment_and_offset_uleb) or (
                        self.opcode == self._root.DyldInfoCommand.BindOpcode.add_address_uleb) or (
                        self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_add_address_uleb) or (
                        self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb)):
                    self.uleb = self._root.Uleb128(self._io, self, self._root)

                if self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb:
                    self.skip = self._root.Uleb128(self._io, self, self._root)

                if self.opcode == self._root.DyldInfoCommand.BindOpcode.set_symbol_trailing_flags_immediate:
                    self.symbol = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")

            @property
            def opcode(self):
                if hasattr(self, '_m_opcode'):
                    return self._m_opcode if hasattr(self, '_m_opcode') else None

                self._m_opcode = self._root.DyldInfoCommand.BindOpcode((self.opcode_and_immediate & 240))
                return self._m_opcode if hasattr(self, '_m_opcode') else None

            @property
            def immediate(self):
                if hasattr(self, '_m_immediate'):
                    return self._m_immediate if hasattr(self, '_m_immediate') else None

                self._m_immediate = (self.opcode_and_immediate & 15)
                return self._m_immediate if hasattr(self, '_m_immediate') else None

        class RebaseData(KaitaiStruct):

            class Opcode(Enum):
                done = 0
                set_type_immediate = 16
                set_segment_and_offset_uleb = 32
                add_address_uleb = 48
                add_address_immediate_scaled = 64
                do_rebase_immediate_times = 80
                do_rebase_uleb_times = 96
                do_rebase_add_address_uleb = 112
                do_rebase_uleb_times_skipping_uleb = 128

            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.items = []
                i = 0
                while True:
                    _ = self._root.DyldInfoCommand.RebaseData.RebaseItem(self._io, self, self._root)
                    self.items.append(_)
                    if _.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.done:
                        break
                    i += 1

            class RebaseItem(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.opcode_and_immediate = self._io.read_u1()
                    if ((self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.set_segment_and_offset_uleb) or (
                            self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.add_address_uleb) or (
                            self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times) or (
                            self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_add_address_uleb) or (
                            self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb)):
                        self.uleb = self._root.Uleb128(self._io, self, self._root)

                    if self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb:
                        self.skip = self._root.Uleb128(self._io, self, self._root)

                @property
                def opcode(self):
                    if hasattr(self, '_m_opcode'):
                        return self._m_opcode if hasattr(self, '_m_opcode') else None

                    self._m_opcode = self._root.DyldInfoCommand.RebaseData.Opcode((self.opcode_and_immediate & 240))
                    return self._m_opcode if hasattr(self, '_m_opcode') else None

                @property
                def immediate(self):
                    if hasattr(self, '_m_immediate'):
                        return self._m_immediate if hasattr(self, '_m_immediate') else None

                    self._m_immediate = (self.opcode_and_immediate & 15)
                    return self._m_immediate if hasattr(self, '_m_immediate') else None

        class ExportNode(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.terminal_size = self._root.Uleb128(self._io, self, self._root)
                self.children_count = self._io.read_u1()
                self.children = [None] * (self.children_count)
                for i in range(self.children_count):
                    self.children[i] = self._root.DyldInfoCommand.ExportNode.Child(self._io, self, self._root)

                self.terminal = self._io.read_bytes(self.terminal_size.value)

            class Child(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                    self.node_offset = self._root.Uleb128(self._io, self, self._root)

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value if hasattr(self, '_m_value') else None

                    _pos = self._io.pos()
                    self._io.seek(self.node_offset.value)
                    self._m_value = self._root.DyldInfoCommand.ExportNode(self._io, self, self._root)
                    self._io.seek(_pos)
                    return self._m_value if hasattr(self, '_m_value') else None

        class BindData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.items = []
                i = 0
                while True:
                    _ = self._root.DyldInfoCommand.BindItem(self._io, self, self._root)
                    self.items.append(_)
                    if _.opcode == self._root.DyldInfoCommand.BindOpcode.done:
                        break
                    i += 1

        class LazyBindData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.items = []
                i = 0
                while not self._io.is_eof():
                    self.items.append(self._root.DyldInfoCommand.BindItem(self._io, self, self._root))
                    i += 1

        @property
        def rebase(self):
            if hasattr(self, '_m_rebase'):
                return self._m_rebase if hasattr(self, '_m_rebase') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.rebase_off)
            self._raw__m_rebase = io.read_bytes(self.rebase_size)
            io = KaitaiStream(BytesIO(self._raw__m_rebase))
            self._m_rebase = self._root.DyldInfoCommand.RebaseData(io, self, self._root)
            io.seek(_pos)
            return self._m_rebase if hasattr(self, '_m_rebase') else None

        @property
        def bind(self):
            if hasattr(self, '_m_bind'):
                return self._m_bind if hasattr(self, '_m_bind') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.bind_off)
            self._raw__m_bind = io.read_bytes(self.bind_size)
            io = KaitaiStream(BytesIO(self._raw__m_bind))
            self._m_bind = self._root.DyldInfoCommand.BindData(io, self, self._root)
            io.seek(_pos)
            return self._m_bind if hasattr(self, '_m_bind') else None

        @property
        def lazy_bind(self):
            if hasattr(self, '_m_lazy_bind'):
                return self._m_lazy_bind if hasattr(self, '_m_lazy_bind') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.lazy_bind_off)
            self._raw__m_lazy_bind = io.read_bytes(self.lazy_bind_size)
            io = KaitaiStream(BytesIO(self._raw__m_lazy_bind))
            self._m_lazy_bind = self._root.DyldInfoCommand.LazyBindData(io, self, self._root)
            io.seek(_pos)
            return self._m_lazy_bind if hasattr(self, '_m_lazy_bind') else None

        @property
        def exports(self):
            if hasattr(self, '_m_exports'):
                return self._m_exports if hasattr(self, '_m_exports') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.export_off)
            self._raw__m_exports = io.read_bytes(self.export_size)
            io = KaitaiStream(BytesIO(self._raw__m_exports))
            self._m_exports = self._root.DyldInfoCommand.ExportNode(io, self, self._root)
            io.seek(_pos)
            return self._m_exports if hasattr(self, '_m_exports') else None

    class DylinkerCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = self._root.LcStr(self._io, self, self._root)

    class DylibCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name_offset = self._io.read_u4le()
            self.timestamp = self._io.read_u4le()
            self.current_version = self._io.read_u4le()
            self.compatibility_version = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")

    class LcStr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4le()
            self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")

    class LoadCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._root.LoadCommandType(self._io.read_u4le())
            self.size = self._io.read_u4le()
            _on = self.type
            if _on == self._root.LoadCommandType.sub_library:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SubCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.segment_split_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.rpath:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.RpathCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.source_version:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SourceVersionCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.encryption_info_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.EncryptionInfoCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.version_min_tvos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.VersionMinCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_dylinker:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylinkerCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.sub_framework:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SubCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_weak_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.version_min_iphoneos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.VersionMinCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.linker_optimization_hint:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dyld_environment:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylinkerCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_upward_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dylib_code_sign_drs:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dyld_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DyldInfoCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.reexport_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.symtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SymtabCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.routines_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.RoutinesCommand64(io, self, self._root)
            elif _on == self._root.LoadCommandType.id_dylinker:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylinkerCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.main:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.EntryPointCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.function_starts:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.version_min_macosx:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.VersionMinCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.data_in_code:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.version_min_watchos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.VersionMinCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.encryption_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.EncryptionInfoCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.sub_umbrella:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SubCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.linker_option:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkerOptionCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.twolevel_hints:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.TwolevelHintsCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.uuid:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.UuidCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dyld_info_only:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DyldInfoCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.lazy_load_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.sub_client:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SubCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.routines:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.RoutinesCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.code_signature:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CodeSignatureCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dysymtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DysymtabCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.segment_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SegmentCommand64(io, self, self._root)
            elif _on == self._root.LoadCommandType.id_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            else:
                self.body = self._io.read_bytes((self.size - 8))

    class UuidCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uuid = self._io.read_bytes(16)

    class SymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sym_off = self._io.read_u4le()
            self.n_syms = self._io.read_u4le()
            self.str_off = self._io.read_u4le()
            self.str_size = self._io.read_u4le()

        class StrTable(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.unknown = self._io.read_u4le()
                self.items = []
                i = 0
                while True:
                    _ = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                    self.items.append(_)
                    if _ == u"":
                        break
                    i += 1

        class Nlist64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.un = self._io.read_u4le()
                self.type = self._io.read_u1()
                self.sect = self._io.read_u1()
                self.desc = self._io.read_u2le()
                self.value = self._io.read_u8le()

        @property
        def symbols(self):
            if hasattr(self, '_m_symbols'):
                return self._m_symbols if hasattr(self, '_m_symbols') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.sym_off)
            self._m_symbols = [None] * (self.n_syms)
            for i in range(self.n_syms):
                self._m_symbols[i] = self._root.SymtabCommand.Nlist64(io, self, self._root)

            io.seek(_pos)
            return self._m_symbols if hasattr(self, '_m_symbols') else None

        @property
        def strs(self):
            if hasattr(self, '_m_strs'):
                return self._m_strs if hasattr(self, '_m_strs') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.str_off)
            self._raw__m_strs = io.read_bytes(self.str_size)
            io = KaitaiStream(BytesIO(self._raw__m_strs))
            self._m_strs = self._root.SymtabCommand.StrTable(io, self, self._root)
            io.seek(_pos)
            return self._m_strs if hasattr(self, '_m_strs') else None

    class VersionMinCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._root.Version(self._io, self, self._root)
            self.sdk = self._root.Version(self._io, self, self._root)

    class EntryPointCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entry_off = self._io.read_u8le()
            self.stack_size = self._io.read_u8le()
