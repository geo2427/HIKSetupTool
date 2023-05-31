# coding:utf-8
import maya.cmds as cmds
import maya.mel as mel
import pymel.all as pm
import os, json


def CreateADVSet(x):
    Control_Set = [
    'Main', 
    'MainExtra1', 
    'MainExtra2', 
    'RootExtraX_M', 
    'RootX_M', 
    'FKExtraToes_R', 
    'FKToes_R', 
    'FKExtraAnkle_R', 
    'FKAnkle_R', 
    'FKExtraKnee_R', 
    'FKKnee_R', 
    'FKExtraHip_R', 
    'FKHip_R', 
    # 'FKExtraEye_R', 
    # 'FKEye_R', 
    'FKExtraJaw_M', 
    'FKJaw_M', 
    'FKExtraHead_M', 
    'FKHead_M', 
    'FKExtraNeck_M', 
    'FKNeck_M', 
    'FKExtraMiddleFinger3_R', 
    'FKMiddleFinger3_R', 
    'FKExtraMiddleFinger2_R', 
    'FKMiddleFinger2_R', 
    'FKExtraMiddleFinger1_R', 
    'FKMiddleFinger1_R', 
    'FKExtraThumbFinger3_R', 
    'FKThumbFinger3_R', 
    'FKExtraThumbFinger2_R', 
    'FKThumbFinger2_R', 
    'FKExtraThumbFinger1_R', 
    'FKThumbFinger1_R', 
    'FKExtraIndexFinger3_R', 
    'FKIndexFinger3_R', 
    'FKExtraIndexFinger2_R', 
    'FKIndexFinger2_R', 
    'FKExtraIndexFinger1_R', 
    'FKIndexFinger1_R', 
    'FKExtraPinkyFinger3_R', 
    'FKPinkyFinger3_R', 
    'FKExtraPinkyFinger2_R', 
    'FKPinkyFinger2_R', 
    'FKExtraPinkyFinger1_R', 
    'FKPinkyFinger1_R', 
    'FKExtraRingFinger3_R', 
    'FKRingFinger3_R', 
    'FKExtraRingFinger2_R', 
    'FKRingFinger2_R', 
    'FKExtraRingFinger1_R', 
    'FKRingFinger1_R', 
    'FKExtraCup_R', 
    'FKCup_R', 
    'FKExtraWrist_R', 
    'FKWrist_R', 
    'FKExtraElbow_R', 
    'FKElbow_R', 
    'FKExtraShoulder_R', 
    'FKShoulder_R', 
    'FKExtraScapula_R', 
    'FKScapula_R', 
    'FKExtraChest_M', 
    'FKChest_M', 
    'FKExtraSpine2_M', 
    'FKSpine2_M', 
    'FKExtraSpine1_M', 
    'FKSpine1_M', 
    'FKExtraRoot_M', 
    'FKRoot_M', 
    'FKExtraToes_L', 
    'FKToes_L', 
    'FKExtraAnkle_L', 
    'FKAnkle_L', 
    'FKExtraKnee_L', 
    'FKKnee_L', 
    'FKExtraHip_L', 
    'FKHip_L', 
    # 'FKExtraEye_L', 
    # 'FKEye_L', 
    'FKExtraMiddleFinger3_L', 
    'FKMiddleFinger3_L', 
    'FKExtraMiddleFinger2_L', 
    'FKMiddleFinger2_L', 
    'FKExtraMiddleFinger1_L', 
    'FKMiddleFinger1_L', 
    'FKExtraThumbFinger3_L', 
    'FKThumbFinger3_L', 
    'FKExtraThumbFinger2_L', 
    'FKThumbFinger2_L', 
    'FKExtraThumbFinger1_L', 
    'FKThumbFinger1_L', 
    'FKExtraIndexFinger3_L', 
    'FKIndexFinger3_L', 
    'FKExtraIndexFinger2_L', 
    'FKIndexFinger2_L', 
    'FKExtraIndexFinger1_L', 
    'FKIndexFinger1_L', 
    'FKExtraPinkyFinger3_L', 
    'FKPinkyFinger3_L', 
    'FKExtraPinkyFinger2_L', 
    'FKPinkyFinger2_L', 
    'FKExtraPinkyFinger1_L', 
    'FKPinkyFinger1_L', 
    'FKExtraRingFinger3_L', 
    'FKRingFinger3_L', 
    'FKExtraRingFinger2_L', 
    'FKRingFinger2_L', 
    'FKExtraRingFinger1_L', 
    'FKRingFinger1_L', 
    'FKExtraCup_L', 
    'FKCup_L', 
    'FKExtraWrist_L', 
    'FKWrist_L', 
    'FKExtraElbow_L', 
    'FKElbow_L', 
    'FKExtraShoulder_L', 
    'FKShoulder_L', 
    'FKExtraScapula_L', 
    'FKScapula_L', 
    # 'AimEye_M', 
    # 'AimEye_R', 
    # 'AimEye_L', 
    'IKExtraLeg_R', 
    'IKLeg_R', 
    'PoleExtraLeg_R', 
    'PoleLeg_R', 
    'IKExtraArm_R', 
    'IKArm_R', 
    'PoleExtraArm_R', 
    'PoleArm_R', 
    'IKLocalExtraArm_R', 
    'IKLocalArm_R', 
    'IKExtracvSpine1_M', 
    'IKcvSpine1_M', 
    'IKExtracvSpine2_M', 
    'IKcvSpine2_M', 
    'IKExtracvSpine3_M', 
    'IKcvSpine3_M', 
    'IKExtracvSpine4_M', 
    'IKcvSpine4_M', 
    'IKExtraSpine1_M', 
    'IKSpine1_M', 
    'IKExtraSpine2_M', 
    'IKSpine2_M', 
    'IKExtraSpine3_M', 
    'IKSpine3_M', 
    'IKhybridExtraSpine1_M', 
    'IKhybridSpine1_M', 
    'IKhybridExtraSpine2_M', 
    'IKhybridSpine2_M', 
    'IKhybridExtraSpine3_M', 
    'IKhybridSpine3_M', 
    'IKExtraLeg_L', 
    'IKLeg_L', 
    'PoleExtraLeg_L', 
    'PoleLeg_L', 
    'IKExtraArm_L', 
    'IKArm_L', 
    'PoleExtraArm_L', 
    'PoleArm_L', 
    'IKLocalExtraArm_L', 
    'IKLocalArm_L', 
    'FKIKLeg_R', 
    'FKIKArm_R', 
    'FKIKSpine_M', 
    'FKIKLeg_L', 
    'FKIKArm_L', 
    'IKLocalExtraLegHip_R', 
    'IKLocalLegHip_R', 
    'IKLocalExtraLegHip_L', 
    'IKLocalLegHip_L', 
    'RollExtraToes_R', 
    'RollToes_R', 
    'RollExtraToesEnd_R', 
    'RollToesEnd_R', 
    'RollExtraHeel_R', 
    'RollHeel_R', 
    'IKExtraToes_R', 
    'IKToes_R', 
    'RollExtraToes_L', 
    'RollToes_L', 
    'RollExtraToesEnd_L', 
    'RollToesEnd_L', 
    'RollExtraHeel_L', 
    'RollHeel_L', 
    'IKExtraToes_L', 
    'IKToes_L', 
    'HipSwinger_M', 
    'BendExtraKnee1_R', 
    'BendKnee1_R', 
    'BendExtraKnee2_R', 
    'BendKnee2_R', 
    'BendExtraHip1_R', 
    'BendHip1_R', 
    'BendExtraHip2_R', 
    'BendHip2_R', 
    'BendExtraElbow1_R', 
    'BendElbow1_R', 
    'BendExtraElbow2_R', 
    'BendElbow2_R', 
    'BendExtraShoulder1_R', 
    'BendShoulder1_R', 
    'BendExtraShoulder2_R', 
    'BendShoulder2_R', 
    'BendExtraKnee1_L', 
    'BendKnee1_L', 
    'BendExtraKnee2_L', 
    'BendKnee2_L', 
    'BendExtraHip1_L', 
    'BendHip1_L', 
    'BendExtraHip2_L', 
    'BendHip2_L', 
    'BendExtraElbow1_L', 
    'BendElbow1_L', 
    'BendExtraElbow2_L', 
    'BendElbow2_L', 
    'BendExtraShoulder1_L', 
    'BendShoulder1_L', 
    'BendExtraShoulder2_L', 
    'BendShoulder2_L', 
    'Fingers_R', 
    'Fingers_L'
    ]

    pm.select(cl=1)
    if pm.objExists('ControlSet'): 
        print('ControlSet이 이미 존재합니다.')
    else:
        pm.select(Control_Set)
        pm.sets(n='ControlSet')
        pm.select(cl=1)
        print('ControlSet을 생성했습니다.')


# Definition 생성
def CHNameField():
    filePath = cmds.file(q=True, sn=True)
    fileName = os.path.basename(filePath)
    ChName = fileName.split('_')[0]
    return ChName


def CreateHIK(CHNameField, x):
    FKIKlist = ['FKIKLeg_R', 'FKIKArm_R', 'FKIKSpine_M', 'FKIKLeg_L', 'FKIKArm_L']
    for ctrl in FKIKlist:
        pm.setAttr(ctrl+'.FKIKBlend', 0)
    mel.eval('hikCreateCharacter("%s")'%(CHNameField()))
    print("HIK 노드가 생성되었습니다.")


# HIK Setting
def LoadCostomHIK(x):
    # # SDK grp 네이밍 변경
    # pm.select('SDKFK*Finger*')
    # SDKGrpList = pm.ls(sl=1)

    # for Gp in SDKGrpList:
    #     if Gp.nodeType() == 'transform':
    #         GpName = Gp.split('_')
    #         if  GpName[-1] == 'L':
    #             pm.rename(Gp.name(), GpName[0]+'_Left')
    #         else:
    #             pm.rename(Gp.name(), GpName[0]+'_Right')
    #     else:
    #         print(Gp)

    # AVS Root Lock 풀기
    Attrlist = ['sx', 'sy', 'sz']
    for att in Attrlist:
        pm.setAttr('RootX_M'+'.'+att, lock=0)
        pm.setAttr('RootX_M'+'.'+att, channelBox=1)
        pm.setAttr('RootX_M'+'.'+att, keyable=1)
    
    pm.select('Main')
    mel.eval('hikNameMatching()')
    mel.eval('hikToggleLockDefinition()')

    print("HIK Assign이 완료되었습니다.")


# Lock ForeArm, Leg Axis
def RotLimitSetting(part, x):
    HIKNode = CHNameField()
    pm.select(HIKNode)
    
    SideList = ['Left', 'Right']
    ValueList = ['Min', 'Max']
    AttrList = ['x', 'y', 'z']
    
    for side in SideList:
        for Valu in ValueList:
            SetValueName = HIKNode+'.'+side+part+Valu
            print (SetValueName)
            for att in AttrList:
                getCheckBox = pm.checkBox(att, q=1, v=1)
                if getCheckBox == 1:
                    pm.setAttr(SetValueName+'RLimitEnable'+att, 0)
                else:
                    pm.setAttr(SetValueName+'RLimitEnable'+att, 1)
                    pm.setAttr(SetValueName+'RLimit'+att, 0)

    print (part+' Rotation Limit 세팅이 완료되었습니다.')


# Set Tpose IK
def mirrorArm(direction):
    ctl = ['PoleArm_%s' % direction, 'FKScapula_%s' % direction, 'IKArm_%s' % direction]
    t = pm.group(n='temp', em=1)
    tG = pm.group(n='tempGrp')
    for i in range(3):
        if direction == "L":
            other = "R"
        else:
            other = "L"
        otherDirection = ctl[i].replace(direction, other)
        pm.setAttr(tG + '.scaleX', 1)
        if not i:
            pm.delete(pm.pointConstraint(ctl[i], t, mo=0))
        else:
            pm.delete(pm.parentConstraint(ctl[i], t, mo=0))
        pm.setAttr(tG + '.scaleX', -1)
        if not i:
            pm.delete(pm.pointConstraint(t, otherDirection, mo=0))
        else:
            pm.delete(pm.parentConstraint(t, otherDirection, mo=0))
    pm.delete(tG)


def SetTposeIK(x):    
    AToB = pm.datatypes.Vector.zero
    armJoint = [['Shoulder_L', 'Elbow_L'], ['Elbow_L', 'Wrist_L']]
    ikHandCtl = 'IKArm_L'
    wrist = pm.PyNode(ikHandCtl)

    for items in armJoint:
        aRev = pm.datatypes.Vector(pm.xform(items[0], q=1, t=1, ws=1)).__neg__()
        b = pm.datatypes.Vector(pm.xform(items[1], q=1, t=1, ws=1))
        AToB += pm.datatypes.Vector.length(aRev+b)
    sholderPoint = pm.datatypes.Vector(pm.xform(armJoint[0][0], q=1, t=1, ws=1))
    goalPoint = sholderPoint+(AToB.x, 0, 0)
    pm.xform(ikHandCtl, t=goalPoint, ws=1)
    ElbowHigh = pm.datatypes.Vector(0, pm.xform(armJoint[0][1], q=1, t=1, ws=1)[1], 0)
    polPos = pm.datatypes.Vector(pm.xform(wrist, q=1, t=1, ws=1))
    wristRo = pm.xform(armJoint[1][1], q=1, os=1, ro=1)
    pm.xform(wrist, t=(polPos.x, ElbowHigh.y, polPos.z), ws=1)
    pm.xform(wrist, os=1, ro=(0, wristRo[1]*-1, wristRo[2]*-1))

    mirrorArm('L')

    pm.setAttr('PoleArm_L.follow', 10)
    pm.setAttr('PoleArm_R.follow', 10)
    pm.setAttr('IKArm_R.rx', 0)


# SAVE POSE
def savePose(poseName, x):


    allCtrl = pm.PyNode('Main')
    try:
        allCtrl.addAttr(poseName, dt='string')
    except:
        allCtrl.setAttr(poseName, lock=0)
        allCtrl.setAttr(poseName, '')
        
    ctrlSetList = pm.listRelatives('ControlSet', children=1)
    crvs = []
    for csl in ctrlSetList:
        if csl.type() ==  'nurbsCurve':
            crvs.append(csl)
        else:
            pass            
        
    ctrls = [crv.getParent() for crv in crvs]
    ctrlVale = {}
    for ctrl in ctrls:
        attrList = ctrl.listAttr(keyable=True)
        for attr in attrList:
            ctrlVale[attr.name()] = attr.get()

    poseValue = json.dumps(ctrlVale, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)

    allCtrl.setAttr(poseName, poseValue)
    allCtrl.setAttr(poseName, lock=1)

    print(poseName + " SAVE가 완료되었습니다.")


# LOAD POSE
def loadPose(poseName, x):
    allCtrl = pm.PyNode('Main')
    data = json.loads(allCtrl.attr(poseName).get())
    
    for key, value in data.items():
        try:
            pm.setAttr(key, value)
        except:
            pass
    
    print(poseName + "를 LOAD 하였습니다.")
