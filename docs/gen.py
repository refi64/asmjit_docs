import os

f_base = '''{name}
{eq}

.. doxygen{type}:: asmjit::{name}
   :project: asmjit
'''

inttypes = [16, 32, 64, 8, 'Ptr']

x86x64_structs = [
  'FpReg',
  'FpVar',
  'GpReg',
  'GpVar',
  'InstInfo',
  'JitRuntime',
  'Mem',
  'MmReg',
  'MmVar',
  'RegCount',
  'RegMask',
  'SegReg',
  'VarInfo',
  'VarState',
  'X86Reg',
  'X86Var',
  'XmmReg',
  'XmmVar',
  'YmmReg',
  'YmmVar']+['X86X64'+n for n in ['Assembler', 'CallNode', 'Compiler', 'FuncDecl', 'FuncNode']]

x86x64_unions = ['CpuId', 'StateCell']

structs = [
  'AlignNode',
  'AutoLock',
  'BaseAssembler',
  'BaseCompiler',
  'BaseCpu',
  'BaseLogger',
  'BaseMem',
  'BaseNode',
  'BaseReg',
  'BaseRuntime',
  'BaseVar',
  'BaseVarInst',
  'BaseVarState',
  'CallNode',
  'CodeGen',
  'CommentNode',
  'EmbedNode',
  'EndNode',
  'FileLogger',
  'FuncBuilderX',
  'FuncDecl',
  'FuncInOut',
  'FuncNode',
  'FuncPrototype',
  'HintNode',
  'Imm',
  'InstNode',
  'JumpNode',
  'Label',
  'LabelData',
  'LabelLink',
  'Lock',
  'MemoryManager',
  'Operand',
  'OperandUtil'
  'PodVector',
  'RelocData',
  'RetNode',
  'SArgNode',
  'StringBuilder',
  'StringLogger',
  'StringUtil',
  'TargetNode',
  'VarBits',
  'VarData',
  'VirtualMemoryManager',
  'VMem',
  'Zone'
  ]+\
  ['FuncBuilder'+str(i) for i in range(11)]+\
  ['Fn'+t for t in\
    ['Double', 'Float', 'Void']+\
      ['UInt'+str(i) for i in inttypes]+\
      ['Int'+str(i) for i in inttypes]]+\
  ['x86x64::'+s for s in x86x64_structs]

unions = ['Vec%dData' % n for n in [64, 128, 256]]+\
  ['x86x64::'+u for u in x86x64_unions]

def getname(f):
    return os.path.join('classes', f.replace('::', '__')+'.rst')

def unname(f):
    return os.path.splitext(os.path.basename(f).replace('__', '::'))[0]

def gettype(x):
    return 'struct' if x in structs else 'union'

def gen():
    for f in os.listdir('classes'):
        fp = os.path.join('classes', f)
        if unname(fp) not in (structs+unions):
            os.remove(fp)
    for x in structs: # no support for unions at the moment
        fp = getname(x)
        if os.path.isfile(fp):
            continue
        out = f_base.format(name=x, eq='='*len(x), type=gettype(x))
        with open(fp, 'w') as f:
            f.write(out)

